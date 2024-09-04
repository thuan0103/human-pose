import cv2
from flask import Flask, Response, request
import threading

app = Flask(__name__)
lock = threading.Lock()  # Sử dụng khóa để đồng bộ hóa truy cập camera

cap = None  # Biến lưu trữ đối tượng VideoCapture toàn cục

def start_capture(url):
    global cap
    with lock:
        if cap is not None:
            cap.release()  # Giải phóng camera hiện tại nếu có
        cap = cv2.VideoCapture(url)

def generate_frames():
    global cap
    while True:
        with lock:
            if cap is None or not cap.isOpened():
                break
            res, image = cap.read()

        if not res:
            print("Không thể đọc khung hình từ webcam")
            break

        ret, buffer = cv2.imencode('.jpg', image)
        image = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + image + b'\r\n')

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

@app.route('/video_feed/<class_name>')
def video_feed(class_name):
    url = ''  # Thay đổi URL camera dựa vào class_name
    if class_name == "D7.04":
        url = 'rtsp://admin:thuandinh0123@192.168.88.114:554/cam/realmonitor?channel=1&subtype=0'
    # Thêm các lớp khác vào đây

    if url:
        start_capture(url)
        return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        return "Class not found", 404

@app.route('/stop_video_feed')
def stop_video_feed():
    global cap
    with lock:
        if cap is not None:
            cap.release()  # Giải phóng camera khi ngừng stream
            cap = None
    return "Video feed stopped", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
