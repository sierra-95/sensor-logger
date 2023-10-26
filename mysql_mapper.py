import mysql.connector
from datetime import datetime
import json

db_config = {
    "host": "localhost",  
    "user": "ubuntu",   
    "password": "Michael@92!7", 
    "database": "sensor_data" 
}
def insert_data_from_file(filename, table_name):
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip()
                try:
                    json_data = json.loads(data)  
                    if table_name == "humidity_data":
                        humidity = json_data["Humidity"]
                        cursor.execute(f"INSERT INTO {table_name} (humidity) VALUES (%s)", (humidity,))
                    elif table_name == "temperature_data":
                        pass
                    elif table_name == "rfid_data":
                        pass
                except json.JSONDecodeError:
                    print(f"Error parsing JSON data from {filename}.")
    except FileNotFoundError:
        print(f"File {filename} not found.")

db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

insert_data_from_file("humidity.txt", "humidity_data")
insert_data_from_file("temperature.txt", "temperature_data")
insert_data_from_file("login.txt", "rfid_data")

db_connection.commit()
db_connection.close()
