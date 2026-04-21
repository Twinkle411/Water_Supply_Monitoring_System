#!/bin/bash

# Creating HDFS directory
hdfs dfs -mkdir -p /water_project

# Uploading dataset to HDFS
hdfs dfs -put brisbane_water_quality.csv /water_project/

# Listing files in HDFS directory
hdfs dfs -ls /water_project

# Checking file size in HDFS
hdfs dfs -du -h /water_project