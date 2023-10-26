import mysql.connector
from datetime import datetime

# MySQL connection configuration
db_config = {
    "host": "localhost",  # Use the host where your MySQL database is running
    "user": "ubuntu",     # Your MySQL username
    "password": "ubuntu", # Your MySQL password
    "database": "sensor_data"  # Your MySQL database name
}

# Function to read data from a file and insert it into the database
def insert_data_from_file(filename, table_name):
    try:
        with open(filename, "r") as file:
            for line in file:
                data = line.strip()  # Read each line from the file
                # Split the data and format as needed for your specific file structure
                # For example, if your humidity.txt and temperature.txt have different structures,
                # you may need to adapt this part accordingly.
                if table_name == "humidity_data":
                    timestamp, humidity = data.split(":")
                    timestamp = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
                    cursor.execute(f"INSERT INTO {table_name} (timestamp, humidity) VALUES (%s, %s)",
                                   (timestamp, humidity))
                elif table_name == "temperature_data":
                    # Handle temperature data format if different from humidity
                    pass
                elif table_name == "rfid_data":
                    # Handle RFID data format if different
                    pass
    except FileNotFoundError:
        print(f"File {filename} not found.")

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(**db_config)
cursor = db_connection.cursor()

# Call the function to insert data from each file into the corresponding table
insert_data_from_file("humidity.txt", "humidity_data")
insert_data_from_file("temperature.txt", "temperature_data")
insert_data_from_file("rfid.txt", "rfid_data")

# Commit the changes and close the connection
db_connection.commit()
db_connection.close()
