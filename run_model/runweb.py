import argparse
import logging
import time
from flask import Flask, Response
import cv2
import numpy as np
import sys
sys.path.append('.')
from tensorflow.keras.models import load_model
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

app = Flask(__name__)

def generate_frames():
    global fps_time
    
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
    cam = cv2.VideoCapture(0,cv2.CAP_DSHOW)  # Update to use RTSP stream URL
    ret_val, image = cam.read()
    logger.info('cam image=%dx%d' % (image.shape[1], image.shape[0]))

    action_model = load_model('action.h5')
    actions = np.array(['quay sang trái','ngồi im','quay sang phải'])
    sequence_length = 50
    keypoints_sequence = []

    while True:
        ret_val, image = cam.read()

        logger.debug('image process+')
        humans = e.inference(image, resize_to_default=(w > 0 and h > 0), upsample_size=args.resize_out_ratio)

        logger.debug('postprocess+')
        image = TfPoseEstimator.draw_humans(image, humans, imgcopy=False)

        for person_id, human in enumerate(humans):
            keypoints = []
            for i in range(18):  # Assume 18 keypoints
                if i in human.body_parts:
                    keypoints.append([human.body_parts[i].x, human.body_parts[i].y])
                else:
                    keypoints.append([0, 0])  # Default value if keypoint is not detected

            # Format keypoints to match the model input shape
            keypoints = np.array(keypoints).flatten()  # Flatten to 1D
            keypoints_sequence.append(keypoints)

            # Ensure we have enough keypoints sequences to match the expected sequence length
            if len(keypoints_sequence) == sequence_length:
                # Prepare input for LSTM (reshape to (sequence_length, feature_size))
                lstm_input = np.array(keypoints_sequence).reshape((1, sequence_length, 36))

                # Make a prediction
                prediction = action_model.predict(lstm_input)
                predicted_action = actions[np.argmax(prediction)]

                # Display the predicted action
                cv2.putText(image, f'Action: {predicted_action}', (10, 50 + 30 * person_id), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
                logger.info(f'Person {person_id} predicted action: {predicted_action}')

                # Remove the first keypoints in the sequence to maintain the sequence length
                keypoints_sequence.pop(0)

        logger.debug('show+')
        cv2.putText(image,
                    "FPS: %f" % (1.0 / (time.time() - fps_time)),
                    (10, 10),  cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 255, 0), 2)
        
        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')

        fps_time = time.time()
        if cv2.waitKey(1) == 27:
            break
        logger.debug('finished+')

    cam.release()

@app.route('/video_feed/A7.06')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
