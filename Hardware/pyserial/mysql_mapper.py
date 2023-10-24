import serial
import json
import mysql.connector
from datetime import datetime

# Define the serial port and baud rate
ser = serial.Serial('com5', 9600)

# Create a function to save data to the MySQL database
def save_data_to_mysql(data):
    # Parse the JSON data
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError:
        print("Invalid JSON data received:", data)
        return

    # Get the current timestamp
    timestamp = datetime.now()

    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",  # Specify your MySQL host
        user="root",  # Specify your MySQL username
        password="Michael@92!7",  # Specify your MySQL password
        database="sensor_data"  # Name of the database you created
    )

    cursor = connection.cursor()

    if 'Humidity' in json_data:
        # Save DHT11 data to the MySQL database
        cursor.execute("INSERT INTO dht11_data (timestamp, humidity, temperatureC, temperatureF, heatIndexC, heatIndexF) VALUES (%s, %s, %s, %s, %s, %s)",
                       (timestamp, json_data['Humidity'], json_data['TemperatureC'], json_data['TemperatureF'], json_data['HeatIndexC'], json_data['HeatIndexF']))

    if 'UID' in json_data:
        # Save RFID data to the MySQL database
        cursor.execute("INSERT INTO rfid_data (timestamp, UID, message) VALUES (%s, %s, %s)",
                       (timestamp, json_data['UID'], json_data['Message']))

    # Commit the changes and close the connection
    connection.commit()
    connection.close()

while True:
    try:
        # Read data from the serial port
        line = ser.readline().decode("utf-8").strip()

        # Save the data to the MySQL database
        save_data_to_mysql(line)

    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        ser.close()
        break
