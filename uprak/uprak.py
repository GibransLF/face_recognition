from koneksi import *
import cv2
import face_recognition
import numpy as np
from datetime import datetime

mycursor.execute("SELECT * FROM user")
users = mycursor.fetchall()

user_data = []

encodings = []

for user in users:
    path_gambar = '../' +user[4]
    
    image = face_recognition.load_image_file(path_gambar)
    encoding = face_recognition.face_encodings(image)[0]
    
    user_data.append({'nama': user[1], 'lahir': user[2], 'jk': user[3], 'img': user[4]})
    encodings.append(encoding)

# Inisialisasi webcam
video_capture = cv2.VideoCapture(0)

while True:
    # Ambil frame dari webcam
    ret, frame = video_capture.read()

    # Ubah frame ke RGB (face_recognition menggunakan RGB)
    rgb_frame = np.ascontiguousarray(frame[:, :, ::-1])

    # Temukan semua wajah dalam frame
    face_locations = face_recognition.face_locations(rgb_frame)
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Loop melalui setiap wajah yang terdeteksi
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Bandingkan wajah dengan gambar referensi
        matches = face_recognition.compare_faces(encodings, face_encoding)
        face_distances = face_recognition.face_distance(encodings, face_encoding)
        
        name = "Tidak diketahui"
        age = "0"
        gender = "Tidak diketahui"
        frame_color = (0, 0, 255)

        if any(matches):
            best_match_index = np.argmin(face_distances)
            
            name = user_data[best_match_index]['nama']
            current_year = datetime.now().year
            age = current_year - user_data[best_match_index]['lahir']
            gender = user_data[best_match_index]['jk']
            frame_color = (0, 255, 0)

        # Gambar kotak di sekitar wajah
        cv2.rectangle(frame, (left, top), (right, bottom), (frame_color), 2)

        # Tambahkan label nama dan umur
        label = f"{name}, {age}, {gender}"
        cv2.putText(frame, label, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Tampilkan hasil
    cv2.imshow('Video', frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan
video_capture.release()
cv2.destroyAllWindows()