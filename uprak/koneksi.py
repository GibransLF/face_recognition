import mysql.connector
import sys

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="fr_mhs",
)

print(mydb)
mycursor = mydb.cursor()
