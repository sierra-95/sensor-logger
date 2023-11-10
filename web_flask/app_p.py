import mysql.connector
from flask import Flask, render_template, request, url_for, redirect

app = Flask(__name__)


db_config = {
    "host": "localhost",
    "user": "ubuntu",
    "password": "Michael@92!7",
    "database": "sensor_logger"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)
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

@app.route('/rfid_from_db')
def rfid_from_db():
    try:
       
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)
        
        cursor.execute("SELECT * FROM rfid_data")
        rfid_data = cursor.fetchall()
        
        cursor.close()
        connection.close()

        return render_template('rfid.html', rfid_data=rfid_data)

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/temperature_from_db')
def temperature_from_db():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        cursor.execute("SELECT * FROM temperature_data")
        temperature_data = cursor.fetchall()

        cursor.close()
        connection.close()

        return render_template('temperature.html', temperature_data=temperature_data)

    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.route('/humidity_from_db')
def humidity_from_db():
    try:
        connection = get_db_connection()
        cursor = connection.cursor(dictionary=True)

        
        cursor.execute("SELECT * FROM humidity_data")
        humidity_data = cursor.fetchall()
       
        cursor.close()
        connection.close()

        return render_template('humidity.html', humidity_data=humidity_data)

    except Exception as e:
        return f"An error occurred: {str(e)}"

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        
        if username == 'sierra-95' and password == 'sierra-95@92!7':          
            return redirect(url_for('index'))
        else:
            error_message = "Incorrect username or password. Please try again."
            return render_template('login.html', error_message=error_message)

   
    return render_template('login.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, ssl_context=('/etc/letsencrypt/live/web-01.holb20233m8xq2.tech/fullchain.pem', '/etc/letsencrypt/live/web-01.holb20233m8xq2.tech/privkey.pem'))
