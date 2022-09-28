import os
import logging

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator

from datetime import datetime

from google.cloud import storage

import pandas as pd
from glom import glom
import json
import gzip
import pickle
import pyarrow.parquet as pq
import pyarrow.csv as pv


path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
url = f"https://fsa-catalogue2.s3.eu-west-2.amazonaws.com/Biotoxin+Results+2021+160322.csv"
file_name_raw = f"Biotoxin+Results+2021+160322.csv"
parquet_file = f"Biotoxin+Results+2021+160322.parquet"

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0,
}

def convert_to_parquet(file_name):
    po = pv.ParseOptions(delimiter=',')
    table = pv.read_csv(file_name, parse_options=po)
    pq.write_table(table, file_name.replace('.csv', '.parquet'))


def upload_to_gcs(bucket, object_name, local_file):

    storage.blob._MAX_MULTIPART_SIZE = 5 * 1024 * 1024  # the maximum size is 5 MB
    storage.blob._DEFAULT_CHUNKSIZE = 5 * 1024 * 1024  

    client = storage.Client()
    bucket = client.bucket(bucket)

    blob1 = bucket.blob(object_name)
    blob1.upload_from_filename(local_file)



with DAG(
    dag_id="data_ingestion",
    schedule_interval="@monthly",
    start_date=datetime(2022, 9, 27),
    default_args=default_args,
    catchup=True,
    max_active_runs=2,
    tags=['final_project_artem'],
) as dag:

    download_dataset_task = BashOperator(
        task_id="download_dataset_task",
        bash_command=f'curl -sSLf {url} > {path_to_local_home}/{file_name_raw}'
    )

    convert_to_parquet_task = PythonOperator(
        task_id="convert_to_parquet_task",
        python_callable=convert_to_parquet,
        op_kwargs={
            "file_name": f"{path_to_local_home}/{file_name_raw}",
        },
    )

    upload_to_gcs_task = PythonOperator(
        task_id="upload_to_gcs_task",
        python_callable=upload_to_gcs,
        op_kwargs={
            "bucket": BUCKET,
            "object_name": f"raw/{parquet_file}",
            "local_file": f"{path_to_local_home}/{parquet_file}",
        },
    )

if __name__ == '__main__':

    download_dataset_task >> convert_to_parquet_task >> upload_to_gcs_task