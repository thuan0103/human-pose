import cv2
import threading
from flask import Flask, Response

app = Flask(__name__)

# URL của camera
url = 'rtsp://admin:thuandinh0123@192.168.88.115:554/cam/realmonitor?channel=1&subtype=0'
cap = cv2.VideoCapture(url)

# Khởi tạo HOG descriptor với bộ phát hiện người tích hợp
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

def detect_motion():
    previous_frame = None
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Không thể đọc khung hình từ webcam")
            break

        # Phát hiện người
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        boxes, weights = hog.detectMultiScale(gray, winStride=(8,8))

        # Kiểm tra chuyển động
        if previous_frame is not None:
            diff = cv2.absdiff(previous_frame, gray)
            non_zero_count = cv2.countNonZero(diff)
            if non_zero_count > 500:  # Ngưỡng để xác định chuyển động
                print("Người đang di chuyển")
            else:
                print("Người đang đứng im")

        previous_frame = gray.copy()

        # Vẽ khung xung quanh người phát hiện
        for (x, y, w, h) in boxes:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

def generate_frames():
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video_feed/D7.04')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    # Tạo thread cho việc phát hiện chuyển động
    t = threading.Thread(target=detect_motion)
    t.start()

    # Chạy Flask app
    app.run(host='0.0.0.0', port=5000)

    # Đợi thread hoàn thành
    t.join()
