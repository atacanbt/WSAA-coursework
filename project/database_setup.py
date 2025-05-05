# database_setup.py
# This script sets up a MySQL database and a table for storing car information.
# It creates a database named 'wsaa' and a table named 'cars' with the specified columns.
# Author: Atacan Buyuktalas

import mysql.connector
from mysql.connector import errorcode
from dbconfig import mysql 

db = mysql.connector.connect(
        host = mysql["host"],
        user = mysql["user"],
        password = mysql["password"],
        database = mysql["database"]
        )
cursor = db.cursor()

cursor.execute("CREATE DATABASE IF NOT EXISTS wsaa")

cursor.execute("USE wsaa")

sql = "CREATE TABLE IF NOT EXISTS cars (" \
    "id INT AUTO_INCREMENT PRIMARY KEY," \
    "brand VARCHAR(50) NOT NULL," \
    "model VARCHAR(50) NOT NULL," \
    "year YEAR NOT NULL," \
    "price DECIMAL(10,2) NOT NULL" \
    ")"

cursor.execute(sql)

cursor.close()
db.close()
print("Database and table setup completed")
