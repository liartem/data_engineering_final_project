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

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

def convert_to_parquet(file_name):
    po = pv.ParseOptions(delimiter=',')
    table = pv.read_csv(file_name, parse_options=po)
    pq.write_table(table, file_name.replace('.csv', '.parquet'))


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
    print_python_version_task = BashOperator(
        task_id="print_python_version",
        bash_command=f'python.__version__()'
    )

if __name__ == '__main__':

    download_dataset_task >> convert_to_parquet_task >> print_python_version_task