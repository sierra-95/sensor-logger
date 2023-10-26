from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/humidity')
def humidity():
    return render_template('humidity.html')

@app.route('/temperature')
def temperature():
    return render_template('temperature.html')

@app.route('/data_visualization')
def data_visualization():
    return render_template('data_visualization.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main':
    app.run(host='0.0.0.0', port='5000')
