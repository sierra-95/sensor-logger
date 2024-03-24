import mysql.connector
from flask import Flask, render_template,request,url_for,redirect
from flask import session


app = Flask(__name__)

# Database connection configuration
db_config = {
    "host": "localhost",
    "user": "ubuntu",
    "password": "Michael@92!7",
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
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        # Check if the provided username and password match
        if username == 'username' and password == 'password':
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
