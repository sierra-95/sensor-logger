import mysql.connector
from flask import Flask, render_template,request

app = Flask(__name__)

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "ubuntu",
    "password": "Michael@92!7",
    "database": "sensor_logger"
}
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/data_visualization')
def data_visualization():
    return render_template('data_visualization.html')
@app.route('/humidity')
def humidity():
    humidity_data = [
        {"timestamp": "2023-11-08 15:30:00", "value": 50.5},
        {"timestamp": "2023-11-08 15:45:00", "value": 55.2},
        {"timestamp": "2023-11-08 16:00:00", "value": 53.7},
        # Add more humidity records as needed
    ]
    return render_template('humidity.html', humidity_data=humidity_data)

@app.route('/rfid')
def rfid():
    rfid_data = [
        {"timestamp": "2023-10-26 16:21:42", "UID": "C1 29 15 31", "Message": "Access granted"},
        {"timestamp": "2023-10-26 16:25:33", "UID": "C1 29 15 31", "Message": "Access granted"},
        {"timestamp": "2023-10-26 23:41:17", "UID": "C1 29 15 31", "Message": "Access granted"},
        {"timestamp": "2023-10-26 23:42:00", "UID": "C1 29 15 31", "Message": "Access granted"},
        # Add more RFID records as needed
    ]
    return render_template('rfid.html', rfid_data=rfid_data)

@app.route('/temperature')
def temperature():
    temperature_data = [
        {"timestamp": "2023-10-26 16:21:49", "TemperatureC": 24.1, "TemperatureF": 75.38, "HeatIndexC": 23.60976, "HeatIndexF": 74.498},
        {"timestamp": "2023-10-26 16:22:19", "TemperatureC": 24.1, "TemperatureF": 75.38, "HeatIndexC": 23.71421, "HeatIndexF": 74.686},
        {"timestamp": "2023-10-26 16:22:49", "TemperatureC": 24.1, "TemperatureF": 75.38, "HeatIndexC": 23.40088, "HeatIndexF": 74.122},
        # Add more temperature records as needed
    ]
    return render_template('temperature.html', temperature_data=temperature_data)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Handle the form submission here, check username and password
        # You can use request.form to access form data
        username = request.form['username']
        password = request.form['password']
        # Add your login logic here

        # If login is successful, you can redirect the user to another page
        if login_is_successful:
            return redirect(url_for('index'))
        else:
            # Handle login failure, perhaps by displaying an error message
            return render_template('login.html', error="Login failed")

    return render_template('login.html')

if __name__ == '__main__':
    app.run()
