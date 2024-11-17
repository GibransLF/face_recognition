import mysql.connector
import sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ml",
)

print(mydb)
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM user")
users = mycursor.fetchall()

nama = []
lahir = []
jk = []
gambar = []

encoding = []