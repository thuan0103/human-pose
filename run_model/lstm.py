import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.utils import to_categorical
from tensorflow.keras.layers import Dropout
from tensorflow.keras.layers import Conv1D, MaxPooling1D, Dropout, BatchNormalization
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint

# Đường dẫn đến thư mục dữ liệu
DATA_PATH = "MAIN_DATA"

# Các hành động và nhãn
actions = np.array(['quay sang trái','ngồi im','quay sang phải'])
label_map = {label: num for num, label in enumerate(actions)}

# Số lượng sequences và độ dài mỗi sequence
no_sequences = 3
sequence_length = 50

# Hàm để đọc dữ liệu từ các file .npy
def load_data():
    sequences, labels = [], []
    for action in actions:
        for sequence in range(no_sequences):
            sequence_data = []
            for frame_num in range(sequence_length):
                frame_data = []
                sequence_path = os.path.join(DATA_PATH, action, str(sequence))
                
                # Đọc dữ liệu keypoints từ từng người (person_id)
                for person_id in os.listdir(sequence_path):
                    npy_path = os.path.join(sequence_path, person_id, f"{frame_num}.npy")
                    if os.path.exists(npy_path):
                        keypoints = np.load(npy_path)
                        frame_data.append(keypoints)

                # Trung bình các keypoints từ nhiều người (nếu cần)
                if frame_data:
                    frame_data = np.mean(frame_data, axis=0)
                else:
                    frame_data = np.zeros((18, 2))  # Giả định có 18 keypoints với tọa độ (x, y)
                sequence_data.append(frame_data)
            
            sequences.append(sequence_data)
            labels.append(label_map[action])
    
    return np.array(sequences), np.array(labels)

# Đọc dữ liệu
x, y = load_data()

# Kiểm tra và reshape lại dữ liệu
x = x.reshape((x.shape[0], sequence_length, -1))  # (số lượng samples, sequence_length, số keypoints * 2)
y = to_categorical(y)

# Chia dữ liệu thành tập huấn luyện và tập kiểm tra
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Xây dựng mô hình LSTM
model = Sequential()
model.add(Conv1D(filters=64, kernel_size=3, activation='relu', input_shape=(sequence_length, 36)))
model.add(MaxPooling1D(pool_size=2))
model.add(Dropout(0.5))  # Thêm Dropout để giảm overfitting
model.add(BatchNormalization())

model.add(LSTM(128, return_sequences=True, activation='relu'))
model.add(Dropout(0.5))  # Thêm Dropout để giảm overfitting
model.add(LSTM(128, return_sequences=False, activation='relu'))

model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))  # Thêm Dropout để giảm overfitting
model.add(Dense(len(actions), activation='softmax'))

# Biên dịch mô hình với học rate và optimizer mới
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Callback functions
early_stopping = EarlyStopping(monitor='val_loss', patience=10, restore_best_weights=True)
model_checkpoint = ModelCheckpoint('best_model.h5', monitor='val_loss', save_best_only=True)

# Huấn luyện mô hình với các callback
history = model.fit(x_train, y_train, epochs=200, validation_data=(x_test, y_test), 
                    batch_size=32)

# Dự đoán và đánh giá mô hình
# Đánh giá mô hình
y_pred = np.argmax(model.predict(x_test), axis=1)
y_true = np.argmax(y_test, axis=1)
print(f"Accuracy: {accuracy_score(y_true, y_pred)}")
model.save("action.h5")

import matplotlib.pyplot as plt

# Lấy dữ liệu từ lịch sử huấn luyện
history_dict = history.history
epochs = range(1, len(history_dict['accuracy']) + 1)

# Vẽ biểu đồ mất mát
plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(epochs, history_dict['loss'], 'b', label='Training loss')
plt.plot(epochs, history_dict['val_loss'], 'r', label='Validation loss')
plt.title('Training and Validation Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()

# Vẽ biểu đồ độ chính xác
plt.subplot(1, 2, 2)
plt.plot(epochs, history_dict['accuracy'], 'b', label='Training accuracy')
plt.plot(epochs, history_dict['val_accuracy'], 'r', label='Validation accuracy')
plt.title('Training and Validation Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()

# Hiển thị biểu đồ
plt.tight_layout()
plt.show()