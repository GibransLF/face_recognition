from koneksi import *

mycursor.execute("SHOW TABLES LIKE 'user'")
user = mycursor.fetchone()

if not user:
    mycursor.execute("""
        CREATE TABLE user(
            id integer AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(255),
            lahir integer(8),
            jk VARCHAR(255),
            img VARCHAR(255)
        )
    """)
    print ("table user berhasil dibuat")
    
    mycursor.execute("""
        INSERT INTO user
            (username, lahir, jk, img) VALUES
                ('Ananta', '2003', 'laki-laki', 'ananta.jpeg'),
                ('Daryat', '1999', 'laki-laki', 'daryat.jpeg'),
                ('Uzi', '2000', 'laki-laki', 'uzi.jpeg')
    """)
    print ("data berhasil ditambahkan")
    mydb.commit()
    
else:
    print ("table user sudah ada")
