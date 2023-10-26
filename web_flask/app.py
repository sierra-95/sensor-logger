from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

db_connection = None

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

@app.route('/')
def home():
    return render_template('/var/www/html/index.html')

@app.route('/humidity')
def humidity():
    cursor = db_connection.cursor()
    cursor.execute("SELECT timestamp, humidity FROM humidity_data")
    humidity_data = cursor.fetchall()
    cursor.close()
    return render_template('/var/www/html/humidity.html', data=humidity_data)

@app.route('/temperature')
def temperature():
    cursor = db_connection.cursor()
    cursor.execute("SELECT timestamp, temperatureC, temperatureF, heatIndexC, heatIndexF FROM temperature_data")
    temperature_data = cursor.fetchall()
    cursor.close()
    return render_template('/var/www/html/temperature.html', data=temperature_data)

@app.route('/data_visualization')
def data_visualization():
    return render_template('/var/www/html/data_visualization.html')

@app.route('/login')
def login():
    return render_template('/var/www/html/login.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=443)

@app.teardown_appcontext
def close_db_connection(exception):
    if db_connection is not None:
        db_connection.close()
