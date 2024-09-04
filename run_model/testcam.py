import cv2
from flask import Flask, Response
app = Flask(__name__)
url = 'rtsp://admin:thuandinh0123@192.168.88.114:554/cam/realmonitor?channel=1&subtype=0'
cap = cv2.VideoCapture(url)
def generate_frames():
    while True:
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
    cap.release()
    cv2.destroyAllWindows()

@app.route('/video_feed/D7.04')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)


