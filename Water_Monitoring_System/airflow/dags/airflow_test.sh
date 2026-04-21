#!/bin/bash

echo " Starting Airflow Pipeline Setup "

# Activate virtual environment
source ~/airflow_env/bin/activate
echo "Virtual environment activated"

# Set Airflow home
export AIRFLOW_HOME=~/airflow
echo "AIRFLOW_HOME set to $AIRFLOW_HOME"

# Initialize DB 
airflow db init
echo "Airflow database initialized"

# Start webserver
echo "Starting Airflow Webserver on port 8080..."
airflow webserver --port 8080 &
WEB_PID=$!

# Start scheduler
echo "Starting Airflow Scheduler..."
airflow scheduler &
SCHED_PID=$!

echo " Airflow is running successfully "
echo " Webserver PID: $WEB_PID "
echo " Scheduler PID: $SCHED_PID "
echo " Open: http://localhost:8080 "

wait