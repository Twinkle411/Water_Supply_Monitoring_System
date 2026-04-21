#!/bin/bash

echo "   Starting Kafka Pipeline Setup   "

KAFKA_PATH=~/kafka_2.13-3.7.0

# Step 1: Start Zookeeper
echo "Starting Zookeeper..."
$KAFKA_PATH/bin/zookeeper-server-start.sh $KAFKA_PATH/config/zookeeper.properties &
ZOOKEEPER_PID=$!

sleep 5

# Step 2: Start Kafka Server
echo "Starting Kafka Broker..."
$KAFKA_PATH/bin/kafka-server-start.sh $KAFKA_PATH/config/server.properties &
KAFKA_PID=$!

sleep 5

# Step 3: Create Topic
echo "Creating topic: water-stream..."
$KAFKA_PATH/bin/kafka-topics.sh --create \
--topic water-stream \
--bootstrap-server localhost:9092 \
--partitions 1 \
--replication-factor 1

echo " Kafka is running successfully "
echo " Zookeeper PID: $ZOOKEEPER_PID "
echo " Kafka PID: $KAFKA_PID "
echo " Topic: water-stream created "

wait