import mysql.connector
import json
from datetime import datetime

# MySQL connection configuration
db_config = {
    "host": "localhost",
    "user": "ubuntu",
    "password": "Michael@92!7",
    "database": "sensor_data"
}

# Function to insert data into the database
def insert_data_to_mysql(filename, table_name):
    try:
        db_connection = mysql.connector.connect(**db_config)
        cursor = db_connection.cursor()

        with open(filename, "r") as file:
            for line in file:
                data = line.strip()
                try:
                    timestamp, json_data = data.split(": ", 1)
                    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                    parsed_data = json.loads(json_data)
                    
                    if table_name == "humidity_data":
                        cursor.execute(
                            f"INSERT INTO {table_name} (date, time, parameter, value) VALUES (%s, %s, %s, %s)",
                            (timestamp.date(), timestamp.time(), "Humidity", parsed_data["Humidity"])
                        )
                    elif table_name == "temperature_data":
                        cursor.execute(
                            f"INSERT INTO {table_name} (date, time, temperature_celsius, temperature_fahrenheit, heat_index_celsius, heat_index_fahrenheit) VALUES (%s, %s, %s, %s, %s, %s)",
                            (timestamp.date(), timestamp.time(), parsed_data["TemperatureC"], parsed_data["TemperatureF"], parsed_data["HeatIndexC"], parsed_data["HeatIndexF"])
                        )
                    elif table_name == "rfid_data":
                        cursor.execute(
                            f"INSERT INTO {table_name} (date, time, parameter1, UID, parameter2, message) VALUES (%s, %s, %s, %s, %s, %s)",
                            (timestamp.date(), timestamp.time(), "UID", parsed_data["UID"], "Message", parsed_data["Message"])
)
                    db_connection.commit()
                except ValueError:
                    print(f"Error parsing data from {filename}")
        
        db_connection.close()

    except mysql.connector.Error as err:
        print(f"MySQL Error: {err}")

# Call the function to insert data from each file into the corresponding table
insert_data_to_mysql("humidity.txt", "humidity_data")
insert_data_to_mysql("temperature.txt", "temperature_data")
insert_data_to_mysql("login.txt", "rfid_data")
