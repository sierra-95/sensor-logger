import serial
import json
from datetime import datetime

# Define the serial port and baud rate
ser = serial.Serial('com5', 9600)

# Create a function to save data to files
def save_data_to_files(data):
    # Parse the JSON data
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError:
        print("Invalid JSON data received:", data)
        return

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    if 'Humidity' in json_data:
        # Save humidity data to humidity.txt
        with open("humidity.txt", "a") as humidity_file:
            humidity_file.write(f"{timestamp}: Humidity = {json_data['Humidity']}%\n")

    if 'TemperatureC' in json_data and 'TemperatureF' in json_data and 'HeatIndexC' in json_data and 'HeatIndexF' in json_data:
        # Save temperature data to temperature.txt
        with open("temperature.txt", "a") as temperature_file:
            temperature_file.write(f"{timestamp}: Temperature (°C) = {json_data['TemperatureC']}, Temperature (°F) = {json_data['TemperatureF']}, Heat Index (°C) = {json_data['HeatIndexC']}, Heat Index (°F) = {json_data['HeatIndexF']}\n")

    if 'UID' in json_data and 'Message' in json_data:
        # Save RFID data to login.txt
        with open("login.txt", "a") as login_file:
            login_file.write(f"{timestamp}: UID = {json_data['UID']}, Message = {json_data['Message']}\n")

while True:
    try:
        # Read data from the serial port
        line = ser.readline().decode("utf-8").strip()

        # Save the data to the respective files
        save_data_to_files(line)

    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        ser.close()
        break
