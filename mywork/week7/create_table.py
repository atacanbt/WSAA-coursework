import mysql.connector
from config import keys as cfg


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = cfg['root'],
    database = "wsaa"
)

cursor = db.cursor()
sql = 'CREATE TABLE cars (id INT AUTO_INCREMENT PRIMARY KEY, brand VARCHAR(50), model VARCHAR(50), year INT(4), price DOUBLE(9,2))'
cursor.execute(sql)

cursor.close()
db.close()