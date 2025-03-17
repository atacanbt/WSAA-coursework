import mysql.connector
from config import keys as cfg


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = cfg['root'],
    database = "wsaa"
)

cursor = db.cursor()
sql = 'UPDATE student SET name = %s, age=%s WHERE id = %s'
val = ('Ali', 33, 3)

cursor.execute(sql, val)
db.commit()

print(cursor.rowcount, "record(s) affected")

cursor.close()
db.close()