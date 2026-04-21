from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
import pandas as pd

def extract():
    df = pd.read_csv("/home/kiit/data/brisbane_water_quality.csv")
    df.to_csv("/tmp/raw.csv", index=False)

def transform():
    df = pd.read_csv("/tmp/raw.csv")
    df = df[["Timestamp", "Temperature", "pH", "Dissolved Oxygen"]]
    df = df[df["Temperature"] > 20]
    df.to_csv("/tmp/processed.csv", index=False)

def load():
    df = pd.read_csv("/tmp/processed.csv")
    df.to_csv("/tmp/final.csv", index=False)

with DAG(
    dag_id="water_etl_pipeline",
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    t1 = PythonOperator(task_id="extract", python_callable=extract)
    t2 = PythonOperator(task_id="transform", python_callable=transform)
    t3 = PythonOperator(task_id="load", python_callable=load)

    t1 >> t2 >> t3
