import cv2
import face_recognition
import numpy as np
from datetime import datetime

# Load gambar referensi
reference_image = face_recognition.load_image_file("foto.jpg")
reference_encoding = face_recognition.face_encodings(reference_image)[0]

# Inisialisasi webcam
video_capture = cv2.VideoCapture(0)

# Informasi pengguna
user_name = "Ananta"
birth_year = 2003

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
        matches = face_recognition.compare_faces([reference_encoding], face_encoding)
        name = "Unknown"
        age = "Unknown"

        # Jika cocok, gunakan nama dan hitung umur
        if matches[0]:
            name = user_name
            current_year = datetime.now().year
            age = current_year - birth_year

        # Gambar kotak di sekitar wajah
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        # Tambahkan label nama dan umur
        label = f"{name}, {age}"
        cv2.putText(frame, label, (left, bottom + 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    # Tampilkan hasil
    cv2.imshow('Video', frame)

    # Tekan 'q' untuk keluar
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Bersihkan
video_capture.release()
cv2.destroyAllWindows()