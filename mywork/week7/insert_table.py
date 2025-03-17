import mysql.connector
from config import keys as cfg


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = cfg['root'],
    database = "wsaa"
)

cursor = db.cursor()
sql = 'INSERT INTO student (name, age) VALUES (%s, %s)'
val = ('Osman', 44)

cursor.execute(sql, val)
db.commit()

print("ID:", cursor.lastrowid)
cursor.close()
db.close()
