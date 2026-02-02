from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from pymongo import MongoClient
import psycopg2

def load_to_postgres():
    mongo = MongoClient("mongodb://mongodb:27017")
    collection = mongo["iot"]["air_quality"]

    pg = psycopg2.connect(
        host="postgres",
        database="analytics",
        user="airflow",
        password="airflow"
    )
    cur = pg.cursor()

    cur.execute("""
    CREATE TABLE IF NOT EXISTS air_quality (
        timestamp TIMESTAMP,
        temperature FLOAT,
        humidity FLOAT,
        pm25 FLOAT
    )
    """)

    for doc in collection.find():
        cur.execute(
            "INSERT INTO air_quality VALUES (%s,%s,%s,%s)",
            (
                doc["timestamp"],
                doc["temperature"],
                doc["humidity"],
                doc["pm25"]
            )
        )

    pg.commit()
    cur.close()
    pg.close()

with DAG(
    dag_id="mongo_to_postgres",
    start_date=datetime(2024, 1, 1),
    schedule_interval="@hourly",
    catchup=False
) as dag:

    transfer = PythonOperator(
        task_id="transfer_data",
        python_callable=load_to_postgres
    )
