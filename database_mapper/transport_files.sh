#!/bin/bash

HUMIDITY_FILE="/home/sierra-95/sensor-logger/humidity.txt"
LOGIN_FILE="/home/sierra-95/sensor-logger/login.txt"
RFID_FILE="/home/sierra-95/sensor-logger/temperature.txt"

SSH_OPTIONS="-i ~/.ssh/id_rsa -o StrictHostKeyChecking=no"

SERVER_USER="ubuntu"
SERVER_IP="174.129.54.202"
DESTINATION_DIR="~/sensor-logger/cron_mover/"

scp $SSH_OPTIONS $HUMIDITY_FILE $SERVER_USER@$SERVER_IP:$DESTINATION_DIR
scp $SSH_OPTIONS $LOGIN_FILE $SERVER_USER@$SERVER_IP:$DESTINATION_DIR
scp $SSH_OPTIONS $RFID_FILE $SERVER_USER@$SERVER_IP:$DESTINATION_DIR

#crontab -e         open chron editor
#*/30 * * * * /path/to/your/files/transport_files.sh         upload every 30 minutes

#scp /path/to/your/files/humidity.txt ubuntu@174.129.54.202:/path/on/server/