import cv2

# Khởi tạo bộ phát hiện người
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())

# Đọc video từ file hoặc camera
cap = cv2.VideoCapture('test.mp4')  
# Lưu vị trí người phát hiện được trong khung hình trước đó
previous_positions = []

# Ngưỡng để xác định xem người có di chuyển hay không
movement_threshold = 10

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    # Phát hiện người trong khung hình
    boxes, weights = hog.detectMultiScale(frame, winStride=(8, 8))
    
    # Lưu vị trí hiện tại của người
    current_positions = []

    for (x, y, w, h) in boxes:
        current_positions.append((x, y, w, h))
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
    # Kiểm tra chuyển động
    if previous_positions:
        for i, (x, y, w, h) in enumerate(current_positions):
            if i < len(previous_positions):
                prev_x, prev_y, prev_w, prev_h = previous_positions[i]
                distance = ((x - prev_x) ** 2 + (y - prev_y) ** 2) ** 0.5
                if distance > movement_threshold:
                    cv2.putText(frame, 'Moving', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
                else:
                    cv2.putText(frame, 'Still', (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)

    # Cập nhật vị trí trước đó
    previous_positions = current_positions
    
    # Hiển thị kết quả
    cv2.imshow('Video', frame)
    
    # Thoát khi nhấn phím 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
