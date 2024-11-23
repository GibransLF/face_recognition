from koneksi import *

mycursor.execute("SHOW TABLES LIKE 'mhs'")
mhs = mycursor.fetchone()

if not mhs:
    mycursor.execute("""
        CREATE TABLE mhs(
            id_mhs integer AUTO_INCREMENT PRIMARY KEY,
            nama_mhs VARCHAR(255),
            tahun_lahir integer(8),
            fakultas VARCHAR(255),
            jurusan VARCHAR(255),
            foto VARCHAR(255)
        )
    """)
    print ("table mhs berhasil dibuat")
    
    mycursor.execute("""
        INSERT INTO mhs
            (nama_mhs, tahun_lahir, fakultas, jurusan, foto) VALUES
                ('Ananta', '2003', 'Fakultas Ilmu Komputer', 'Sistem Informasi', 'ananta.jpeg'),
                ('Daryat', '1999', 'Fakultas Ilmu Komputer', 'Teknik Informatika', 'daryat.jpeg'),
                ('Uzi', '2000', 'Fakultas Ilmu Komputer', 'Teknik Informatika', 'uzi.jpeg')
    """)
    print ("data berhasil ditambahkan")
    mydb.commit()
    
else:
    print ("table mhs sudah ada")
