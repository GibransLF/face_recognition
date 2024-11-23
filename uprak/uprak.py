from koneksi import *
import cv2
import face_recognition
import numpy as np
from datetime import datetime

mycursor.execute("SELECT * FROM mhs")
mahasiswas = mycursor.fetchall()

mhs_data = []

encodings = []

for mhs in mahasiswas:
    path_gambar = '../' +mhs[5]
    
    image = face_recognition.load_image_file(path_gambar)
    encoding = face_recognition.face_encodings(image)[0]
    
    mhs_data.append({'nama_mhs': mhs[1], 'tahun_lahir': mhs[2], 'fakultas': mhs[3], 'jurusan': mhs[4]})
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
            
            name = mhs_data[best_match_index]['nama_mhs']
            current_year = datetime.now().year
            age = current_year - mhs_data[best_match_index]['tahun_lahir']
            fakultas = mhs_data[best_match_index]['fakultas']
            jurusan = mhs_data[best_match_index]['jurusan']
            frame_color = (0, 255, 0)

        # Gambar kotak di sekitar wajah
        cv2.rectangle(frame, (left, top), (right, bottom), (frame_color), 2)

        # Tambahkaan Label
        cv2.putText(frame, fakultas, (left, top - 30), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        cv2.putText(frame, jurusan, (left, top - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
        labelBottom = f"{name}, {age} Tahun"
        cv2.putText(frame, labelBottom, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Tampilkan hasil
    cv2.imshow('Video', frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan
video_capture.release()
cv2.destroyAllWindows()
