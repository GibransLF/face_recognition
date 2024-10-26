# face_recognition simple Python
pengenalan wajah menggunakan img yang disiapkan dan menampilkan tahun

## Install dasar
Pastikan anda sudah menginstall python
saya menggunakan versi python 3.8.8
cek versi menggunakan
```
python --version
```

##atau anda bisa menggunakan venv (Virtual Environment)

jika saat anda menginstall python dan sudah menyentang Path
1. cari di folder 
```
C:\Users\NamaUser\AppData\Local\Programs\Python
```
2. Buka Folder versi python yang anda inginkan
3. pada folder ada
```
python.exe
```
dulpikasi file exe dengan nama versi contoh saya menggunakan 3.8.8

```
python38.exe
```

lalu jalankan terminal di tempat folder "main.py"
untuk membuat venv
```
python38 -m venv venv38
```

untuk masuk menggunakan venv
```
.\venv313\Scripts\activate
```
untuk menghentikan
```
deactivate
```

setelah anda membaca "cara menggunakan" di bawah, untuk menjalankan main.py di venv
```
.\venv38\Scripts\python.exe main.py
```

## Cara menggunakan
1. siapkan gambar wajah, dan berikan nama "foto.jpg" di satu folder yang sama pada main.py
2. ubah data yang di inginkan didalam script main.py
```
# Informasi pengguna
user_name = "Ananta"
birth_year = 2003
```

3. Instalasi
jalankan di terminal
```
pip install face-recognition
pip install numpy
pip install opencv-python
pip install dlib
```

4. Jalankan Script
jalankan di terminal
```
python main.py
```
Selesai
