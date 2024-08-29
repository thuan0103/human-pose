import cv2
url = 'rtsp://admin:vietson150@192.168.0.107:554/cam/realmonitor?channel=1&subtype=0'
cap = cv2.VideoCapture(0,cv2.CAP_DSHOW)

while True:
    res, frame = cap.read()

    if not res:
        print("Không thể đọc khung hình từ webcam")
        break

    cv2.imshow('tf-pose-estimation result', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

