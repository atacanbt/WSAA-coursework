import mysql.connector
from config import keys as cfg


db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = cfg['root']
)

cursor = db.cursor()

cursor.execute("CREATE DATABASE wsaa;")

cursor.close()
db.close()