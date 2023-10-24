import mysql.connector

connection = mysql.connector.connect(
    host="172.16.119.58 ",
    user="ubuntu",
    password="ubuntu",
    database="sensor_data"
)
if connection.is_connected():
    print("Database connection is active.")
else:
    print("Database connection is not active.")
connection.close()
