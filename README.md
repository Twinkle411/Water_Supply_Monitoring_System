# Water Supply Monitoring System

An end-to-end Data Engineering pipeline designed to monitor, process, and visualize water quality data using batch and streaming techniques.

This project demonstrates how raw water quality data can be ingested, processed using distributed systems, and presented through an interactive dashboard for real-time insights. Applied on " brisbane_water_quality " dataset .

The system simulates a real-world water monitoring pipeline by integrating multiple data engineering tools. It processes structured CSV data, applies transformations, and visualizes key metrics like pH and turbidity.

##  Technology Stack

* **Data Processing:** Python, Pandas, PySpark
* **Streaming:** Apache Kafka
* **Storage:** HDFS , PostgreSQL
* **Orchestration:** Apache Airflow
* **Frontend Dashboard:** Streamlit
* **Scripting & Automation:** Shell Scripts

## Workflow Architecture

```id="flow1"
CSV Data → Ingestion → Spark Processing → Kafka Streaming → Storage → Dashboard
```

##  Project Structure

```id="struct1"
Water_Monitoring_System/
│
├── airflow/                # DAG for pipeline automation
├── dashboard/              # Streamlit dashboard
├── data/                   # Input dataset
├── data_quality/           # Data validation scripts
├── database/               # Data ingestion notebooks
├── final/                  # Final processed output
├── hdfs/                   # HDFS scripts
├── kafka/                  # Kafka producer/consumer
├── scripts/                # Utility scripts
├── spark/                  # Spark processing
├── streaming/              # Streaming simulation
```

## How to Run the Project

### 1. Install Dependencies

```id="run1"
pip install streamlit pandas
```

### 2. Run Dashboard

```id="run2"
python3 -m streamlit run dashboard/dashboard.py
```

##  Login Credentials

```id="login1"
Username: admin  
Password: admin123
```
( Navigate to Local URL: http://localhost:8501
  Network URL: http://172.25.223.28:8501 )
  
##  Features

* Water quality data visualization
* pH and turbidity monitoring
* Batch + streaming pipeline simulation
* ETL and ELT pipelines
* OLTP and OLAP sytems
* Modular and scalable architecture
* Simple interactive dashboard
  
##  Unique Highlights

* Integration of multiple Big Data tools (Spark, Kafka, Airflow)
* Combination of batch and streaming concepts
* Clean and modular pipeline design
* Lightweight frontend for quick insights

##  Future Enhancements

* Real-time IoT sensor integration
* Cloud deployment (AWS/GCP)
* Alert system for unsafe water levels
* Machine learning-based predictions
