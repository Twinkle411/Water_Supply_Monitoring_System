#!/bin/bash

# Water Supply Monitoring System Pipeline

mkdir -p raw data logs

echo " Water Supply Monitoring System Pipeline Started"

# Check sensor data from water tanks / pipelines
if ls raw/*.csv 1> /dev/null 2>&1; then
    
    # Move sensor data to processing folder
    mv raw/*.csv data/

    # Log successful transfer
    echo "[$(date)] Sensor data moved from FIELD (raw) to PROCESSING (data)" >> logs/water_pipeline.log

    echo " Sensor data processed successfully"

else
    # Log missing sensor data
    echo "[$(date)] ALERT: No sensor data received from field devices" >> logs/water_pipeline.log

    echo "No sensor data found"
fi
