import mysql.connector

connection = mysql.connector.connect(
    host="41.89.227.171 ",
    user="ubuntu",
    password="ubuntu",
    database="sensor_data"
)
if connection.is_connected():
    print("Database connection is active.")
else:
    print("Database connection is not active.")
connection.close()
