import mysql.connector

connection = mysql.connector.connect(
    host="localhost",
    user="ubuntu",
    password="Michael@92!7",
    database="sensor_data"
)
if connection.is_connected():
    print("Database connection is active.")
else:
    print("Database connection is not active.")
connection.close()
