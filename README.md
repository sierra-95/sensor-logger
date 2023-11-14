<<<<<<< HEAD
**The Sensor Logger**
=======
## The Sensor Logger
>>>>>>> 91a2726390432595df08e3596bf82a3edeee1614

Welcome to the Sensor Logger project!
This webpage serves as the gateway to our innovative real-time sensor data monitoring and visualization platform.
![Screenshot 2023-11-08 115645](https://github.com/sierra-95/sensor-logger/assets/111045570/b1ed9d29-fa55-4693-b8a8-7f9bc33d60e2)

## Table of Content
* [Introduction](#introduction)
* [Environment](#environment)
* [Installation](#installation)
* [Bugs](#bugs)
* [Authors](#authors)
* [License](#license)

## Introduction:
Our landing page introduces you to the world of Sensor Logger.
This project was inspired by a personal experience where the need for real-time data collection became apparent.
We observed the challenges of manual data collection and saw the opportunity to create a solution that would make data collection effortless and efficient.

## Key Features
1. Real-time Sensor Data: Sensor Logger allows you to access sensor data in real-time, empowering you with immediate insights into your connected devices.
2. Easy Navigation: The landing page provides a user-friendly interface with easy navigation elements. You can explore different sections, including an "About" section to learn more about the project's background.
3. Interactive Visuals: We believe in making data more understandable. As you navigate through the page, you'll find interactive visuals and images that showcase our project's potential.
4. Project Story: We've added a personal touch to the project with a story that inspired it. This isn't just another project; it's a journey that began with a real-world problem and evolved into a high-tech solution.

**Getting Started:**
To access our full platform, click on https://sierra-95.github.io/ or the "View Sensor Dashboard" button in the header. This will take you to the complete Sensor Logger application where you can explore and interact with sensor data in real time.

## Getting Started:
To access our landing page, click on https://sierra-95.github.io/ and get more concise explanations about the sensor logger.
To view a sample sensor logger dashboard, click on https://web-01.holb20233m8xq2.tech/. This will take you to the complete Sensor Logger application where you can explore and interact with sensor data in real time.
## Environment
This project is interpreted/tested on Ubuntu 20.04 LTS using python3 (version 3.4.3)

## Installation
* This project assumes you are collecting data on a local machine and uploading the data on a remote server to display it on a website.
* Clone this repository: `git clone "https://github.com/sierra-95/sensor-logger.git"`
* Access Sensor-logger: `cd sensor-logger`

* Confirm you have the following installed on your machine : 
    1. gunicorn         pip install gunicorn
    2. flask            pip install flask
    3. Arduino IDE      https://support.arduino.cc/hc/en-us/articles/360019833020-Download-and-install-Arduino-IDE
    4. mysql.connector  pip install mysql-connector-python
    5. MySQL server     apt-get mysql-server
* Review the following files and edit database and server details.
    1. /sensor-logger/mysql_mapper.py
    2. /sensor-logger/Database/transport_files.sh
    3. /sensor-logger/web_flask/app.py
    **Locally**
* Navigate to /sensor-logger/setup and use sql files to setup your database.
* Open Arduin0 IDE, navigate to /sensor-logger/Hardware/Full_code/ and upload the code to the sensor setup
* Navigate to /sensor-logger/Hardware/PySerial and run collect_data.py
* Follow the setup file at  /sensor-logger/setup/setup-cron-scheduler to setup cron for file upload
* If cron setup fails, use /sensor-logger/Database/transport_files.sh to move files manually.

    **server**
* Clone this repository: `git clone "https://github.com/sierra-95/sensor-logger.git"`
* Follow the setup file on /sensor-logger/setup/setup-flask-server to setup flask
* Configure your server to act as reverse proxy. Reference using : /sensor-logger/web_flask/sensor_logger
* If any need to setup systemctl with flask, use /sensor-logger/web_flask/sensor_logger.service

**Conclusion:**
Sensor Logger is not just a project; it's a solution to a real-world problem. We're excited to share this innovative platform with you and invite you to join us on this data-driven discovery journey. Together, we're pushing the boundaries of data security, user-friendly access, and endless possibilities.

## Bugs
No known bugs at this time. 

## Authors
Michael Machohi -[GitHub](https://github.com/sierra-95) 
## License
Public Domain. No copy write protection. 

