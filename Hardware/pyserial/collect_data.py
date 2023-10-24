import serial
import json

# Define the serial port and baud rate
ser = serial.Serial('com5', 9600)

# Create functions to save data to the respective files
def save_dht11_data(data):
    with open('data.txt', 'a') as file:
        file.write(data + '\n')

def save_rfid_data(data):
    with open('login.txt', 'a') as file:
        file.write(data + '\n')

while True:
    try:
        # Read data from the serial port
        line = ser.readline().decode("utf-8").strip()
        
        # Check if the received data is a valid JSON
        try:
            json_data = json.loads(line)
        except json.JSONDecodeError:
            print("Invalid JSON data received:", line)
            continue

        # Print the received JSON data for verification
        print("Received JSON data:", json_data)

        # Check if the JSON data has 'Humidity' key (DHT11 data)
        if 'Humidity' in json_data:
            # Save DHT11 data to 'data.txt'
            save_dht11_data(line)

        # Check if the JSON data has 'UID' key (RFID data)
        if 'UID' in json_data:
            # Save UID data to 'logic.txt'
            save_rfid_data(line)

    except KeyboardInterrupt:
        # Exit the loop if Ctrl+C is pressed
        ser.close()
        break
