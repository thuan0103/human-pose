import argparse
import logging
import time
import os
import cv2
import numpy as np
import sys
sys.path.append('.')
from tf_pose.estimator import TfPoseEstimator
from tf_pose.networks import get_graph_path, model_wh

logger = logging.getLogger('TfPoseEstimator-WebCam')
logger.setLevel(logging.DEBUG)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s')
ch.setFormatter(formatter)
logger.addHandler(ch)

fps_time = 0

def str2bool(v):
    return v.lower() in ("yes", "true", "t", "1")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='tf-pose-estimation realtime webcam')
    parser.add_argument('--camera', type=int, default=0)
    parser.add_argument('--resize', type=str, default='0x0',
                        help='if provided, resize images before they are processed. default=0x0, Recommends : 432x368 or 656x368 or 1312x736 ')
    parser.add_argument('--resize-out-ratio', type=float, default=4.0,
                        help='if provided, resize heatmaps before they are post-processed. default=1.0')
    parser.add_argument('--model', type=str, default='mobilenet_thin', help='cmu / mobilenet_thin / mobilenet_v2_large / mobilenet_v2_small')
    parser.add_argument('--show-process', type=bool, default=False,
                        help='for debug purpose, if enabled, speed for inference is dropped.')
    parser.add_argument('--tensorrt', type=str, default="False",
                        help='for tensorrt process.')
    args = parser.parse_args()

    logger.debug('initialization %s : %s' % (args.model, get_graph_path(args.model)))
    w, h = model_wh(args.resize)
    if w > 0 and h > 0:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(w, h), trt_bool=str2bool(args.tensorrt))
    else:
        e = TfPoseEstimator(get_graph_path(args.model), target_size=(432, 368), trt_bool=str2bool(args.tensorrt))
    logger.debug('cam read+')
    url = 'rtsp://admin:vietson150@192.168.0.107:554/cam/realmonitor?channel=1&subtype=0'
    cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
    ret_val, image = cam.read()
    logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))

    DATA_PATH = os.path.join("MAIN_DATA")

    actions = np.array(['quay sang trái','ngồi im','quay sang phải'])
    no_sequences = 3
    sequence_length = 50

    for action in actions:
        for sequence in range(no_sequences):
            try:
                os.makedirs(os.path.join(DATA_PATH, action, str(sequence)), exist_ok=True)
            except:
                pass

    label_map = {label: num for num, label in enumerate(actions)}

    obj_id = 0
    for action in actions:
        print(action)
        time.sleep(5)
        for sequence in range(no_sequences):
            print(sequence)
            time.sleep(3)
            for frame_num in range(sequence_length):
                ret_val, image = cam.read()

                logger.debug('image process+')
                humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)

                logger.debug('postprocess+')
                image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

                logger.debug('show+')
                no_pepole = len(humans)
                cv2.putText(image,
                            "FPS: %f" % (1.0 / (time.time() - fps_time)),
                            (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (0, 255, 0), 2)
                cv2.imshow('tf-pose-estimation result', image)
                fps_time = time.time()

                if frame_num == 0:
                    cv2.putText(image, "Bắt đầu thu thập hình ảnh", (120, 200), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, cv2.LINE_AA)
                    cv2.putText(image, f"Thu thập khung hình cho {action} video số {sequence}", (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)
                    time.sleep(2)
                else:
                    cv2.putText(image, f"Thu thập khung hình cho {action} video số {sequence}", (15, 12), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA)

                for person_id, human in enumerate(humans):
                    keypoints = []
                    for i in range(18):  # Giả sử bạn biết có 18 keypoints
                        if i in human.body_parts:
                            keypoints.append((human.body_parts[i].x, human.body_parts[i].y))
                        else:
                            keypoints.append((0, 0))  # Điền giá trị mặc định nếu không phát hiện được điểm keypoint
                    print(keypoints)
                    person_path = os.path.join(DATA_PATH, action, str(sequence),str(person_id))
                    os.makedirs(person_path, exist_ok=True)
                    npy_path = os.path.join(person_path, f"{frame_num}.npy")
                    np.save(npy_path, np.array(keypoints))

                if cv2.waitKey(1) == 27:
                    break
                logger.debug('finished+')

    cv2.destroyAllWindows()