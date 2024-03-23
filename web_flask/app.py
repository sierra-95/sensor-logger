import mysql.connector
from flask import Flask, render_template,request,url_for,redirect
from flask import session


app = Flask(__name__)

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "ubuntu",
    "password": "########",
    "database": "sensor_logger"
}
@app.route('/flask')
def flask_route():
    return "Hello from Flask"
@app.route('/')
def root():
    return redirect(url_for('login'))
@app.route('/index')
def index():
    
    return render_template('index.html')
@app.route('/data_visualization')
def data_visualization():
    return render_template('data_visualization.html')
@app.route('/humidity')
def humidity():
    
    humidity_data = [
        {"date": "2023-10-26", "time": "16:25:33", "value": 42},
        {"date": "2023-10-26", "time": "16:26:03", "value": 45},
        {"date": "2023-10-26", "time": "23:40:04", "value": 78},
        {"date": "2023-10-26", "time": "23:40:34", "value": 69},
        {"date": "2023-10-26", "time": "23:41:04", "value": 48},
        {"date": "2023-10-26", "time": "23:41:34", "value": 53},
        {"date": "2023-10-26", "time": "23:42:04", "value": 42},
        {"date": "2023-10-26", "time": "23:42:34", "value": 46},
        {"date": "2023-10-26", "time": "23:43:04", "value": 28},
        {"date": "2023-10-26", "time": "23:43:34", "value": 32},
        {"date": "2023-10-26", "time": "23:44:04", "value": 28},
    ]
    return render_template('humidity.html', humidity_data=humidity_data)



@app.route('/rfid')
def rfid():
    rfid_data = [
    {"timestamp": "2023-10-26 16:21:42", "UID": "C1 29 15 31", "Message": "Access granted"},
    {"timestamp": "2023-10-26 16:25:33", "UID": "C1 29 15 31", "Message": "Access granted"},
    {"timestamp": "2023-10-26 23:41:17", "UID": "C1 29 15 31", "Message": "Access granted"},
    {"timestamp": "2023-10-26 23:42:00", "UID": "C1 29 15 31", "Message": "Access granted"},
    {"timestamp": "2023-10-26 23:42:33", "UID": "69 58 B5 63", "Message": "Access denied"},
    {"timestamp": "2023-10-26 23:43:59", "UID": "69 58 B5 63", "Message": "Access denied"},
    {"timestamp": "2023-10-26 23:45:27", "UID": "C1 29 15 31", "Message": "Access granted"},
    {"timestamp": "2023-10-31 11:36:55", "UID": "04 70 20 DA BF 6C 80", "Message": "Access denied"}
]

    return render_template('rfid.html', rfid_data=rfid_data)

@app.route('/temperature')
def temperature():
    temperature_data = [
    {"timestamp": "2023-10-26 16:21:49", "TemperatureC": 24.1, "TemperatureF": 75.38, "HeatIndexC": 23.60976, "HeatIndexF": 74.498},
    {"timestamp": "2023-10-26 16:22:19", "TemperatureC": 24.1, "TemperatureF": 75.38, "HeatIndexC": 23.71421, "HeatIndexF": 74.686},
    {"timestamp": "2023-10-26 16:22:49", "TemperatureC": 24.1, "TemperatureF": 75.38, "HeatIndexC": 23.40088, "HeatIndexF": 74.122},
    {"timestamp": "2023-10-26 23:40:04", "TemperatureC": 23.6, "TemperatureF": 74.48, "HeatIndexC": 24.05198, "HeatIndexF": 75.294},
    {"timestamp": "2023-10-26 23:41:04", "TemperatureC": 23.6, "TemperatureF": 74.48, "HeatIndexC": 23.26865, "HeatIndexF": 73.884},
    {"timestamp": "2023-10-26 23:41:34", "TemperatureC": 23.7, "TemperatureF": 74.66, "HeatIndexC": 23.50921, "HeatIndexF": 74.317},
    {"timestamp": "2023-10-26 23:42:04", "TemperatureC": 23.7, "TemperatureF": 74.66, "HeatIndexC": 23.22199, "HeatIndexF": 73.8},
    {"timestamp": "2023-10-26 23:42:34", "TemperatureC": 23.7, "TemperatureF": 74.66, "HeatIndexC": 23.32644, "HeatIndexF": 73.98801},
    {"timestamp": "2023-10-26 23:43:04", "TemperatureC": 23.8, "TemperatureF": 74.84, "HeatIndexC": 22.96643, "HeatIndexF": 73.34},
    {"timestamp": "2023-10-26 23:43:34", "TemperatureC": 23.8, "TemperatureF": 74.84, "HeatIndexC": 23.07088, "HeatIndexF": 73.52799},
    {"timestamp": "2023-10-26 23:44:04", "TemperatureC": 23.8, "TemperatureF": 74.84, "HeatIndexC": 22.96643, "HeatIndexF": 73.34},
    {"timestamp": "2023-10-26 23:44:34", "TemperatureC": 23.8, "TemperatureF": 74.84, "HeatIndexC": 22.99254, "HeatIndexF": 73.38699},
    {"timestamp": "2023-10-26 23:45:04", "TemperatureC": 23.8, "TemperatureF": 74.84, "HeatIndexC": 22.94032, "HeatIndexF": 73.29299},
    {"timestamp": "2023-10-26 23:45:34", "TemperatureC": 23.9, "TemperatureF": 75.02, "HeatIndexC": 23.05032, "HeatIndexF": 73.49099}
]
    return render_template('temperature.html', temperature_data=temperature_data)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the provided username and password match
        if username == 'sierra-95' and password == 'sierra-95@92!7':
            # Successful login, redirect to index.html
            return redirect(url_for('index'))
        else:
            # Incorrect login, render the login page with an error message
            error_message = "Incorrect username or password. Please try again."
            return render_template('login.html', error_message=error_message)

    # Render the login page for GET requests
    return render_template('login.html')





if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=('/etc/letsencrypt/live/web-01.holb20233m8xq2.tech/fullchain.pem', '/etc/letsencrypt/live/web-01.holb20233m8xq2.tech/privkey.pem'))
