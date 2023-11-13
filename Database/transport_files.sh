#!/bin/bash

HUMIDITY_FILE="/sensor-logger/humidity.txt"
LOGIN_FILE="/sensor-logger/login.txt"
RFID_FILE="/sensor-logger/temperature.txt"

SSH_OPTIONS="-i ~/.ssh/id_rsa -o StrictHostKeyChecking=no"

SERVER_USER="ubuntu"
SERVER_IP="set server ip"
DESTINATION_DIR="~/sensor-logger/cron_mover/"

scp $SSH_OPTIONS $HUMIDITY_FILE $SERVER_USER@$SERVER_IP:$DESTINATION_DIR
scp $SSH_OPTIONS $LOGIN_FILE $SERVER_USER@$SERVER_IP:$DESTINATION_DIR
scp $SSH_OPTIONS $RFID_FILE $SERVER_USER@$SERVER_IP:$DESTINATION_DIR



