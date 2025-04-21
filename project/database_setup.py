# database_setup.py
# This script sets up a MySQL database and a table for storing car information.
# It creates a database named 'wsaa' and a table named 'cars' with the specified columns.
import mysql.connector
from mysql.connector import errorcode
from config import keys 

db = mysql.connector.connect(
        host = keys["host"],
        user = keys["user"],
        password = keys["root"],
        database = keys["database"]
        )
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS wsaa")

cursor.execute("USE wsaa")

sql = "CREATE TABLE IF NOT EXISTS cars (id INT AUTO_INCREMENT PRIMARY KEY," \
    "brand VARCHAR(50) NOT NULL,model VARCHAR(50) NOT NULL,year YEAR NOT NULL," \
    "price DECIMAL(10,2) NOT NULL,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP," \
    "last_updated TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"
        
cursor.execute(sql)

cursor.close()
db.close()
print("Database and table setup completed")
