#!/usr/bin/env python3
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# Define the database connection outside of the app context
db_connection = None

def setup_db_connection():
    global db_connection
    try:
        db_connection = mysql.connector.connect(
            host="localhost",
            user="ubuntu",
            password="Michael@92!7",
            database="sensor_data"
        )
        if db_connection.is_connected():
            print("Database connection is active.")
    except mysql.connector.Error as e:
        print(f"Error connecting to the database: {e}")

# Call setup_db_connection before the first request
setup_db_connection()

@app.route('/')
def home():
    return render_template('/var/www/html/index.html')

@app.route('/humidity')
def humidity():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM humidity_data")  # Select all columns
    humidity_data = cursor.fetchall()
    cursor.close()
    return render_template('/var/www/html/humidity.html', data=humidity_data)

@app.route('/temperature')
def temperature():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM temperature_data")  # Select all columns
    temperature_data = cursor.fetchall()
    cursor.close()
    return render_template('/var/www/html/temperature.html', data=temperature_data)


@app.route('/data_visualization')
def data_visualization():
    return render_template('/var/www/html/data_visualization.html')

@app.route('/login')
def login():
    cursor = db_connection.cursor()
    cursor.execute("SELECT * FROM rfid_data")  # Select all columns
    login_data = cursor.fetchall()
    cursor.close()
    return render_template('/var/www/html/login.html', data=login_data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
