import serial
import json
from datetime import datetime

# Define the serial port and baud rate
ser = serial.Serial('com5', 9600)

def save_data_to_files(data):
    # Parse the JSON data
    try:
        json_data = json.loads(data)
    except json.JSONDecodeError:
        print("Invalid JSON data received:", data)
        return

    # Get the current timestamp
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Check for 'Humidity' data and save it to humidity.txt
    if 'Humidity' in json_data:
        with open('humidity.txt', 'a') as file:
            file.write(f"{timestamp}: {{\"Humidity\":{json_data['Humidity']}}}\n")

    # Check for 'TemperatureC' data and save it to temperature.txt
    if 'TemperatureC' in json_data and 'TemperatureF' in json_data and 'HeatIndexC' in json_data and 'HeatIndexF' in json_data:
        with open('temperature.txt', 'a') as file:
            file.write(f"{timestamp}: {{\"TemperatureC\":{json_data['TemperatureC']},\"TemperatureF\":{json_data['TemperatureF']},\"HeatIndexC\":{json_data['HeatIndexC']},\"HeatIndexF\":{json_data['HeatIndexF']}}}\n")
    if 'UID' in json_data:
        with open('login.txt', 'a') as file:
            file.write(f"{timestamp}: {{\"UID\":\"{json_data['UID']}\",\"Message\":\"{json_data['Message']}\"}}\n")
while True:
    try:
        # Read data from the serial port
        line = ser.readline().decode("utf-8").strip()

        # Save the data to the appropriate text files
        save_data_to_files(line)

    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        ser.close()
        break
