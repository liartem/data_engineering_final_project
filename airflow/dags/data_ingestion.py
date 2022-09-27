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



path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
url = f"https://www.dropbox.com/s/noo917u08zphu6e/youtube-reviews-and-unboxing-videos.pickle?dl=1"
file_name = f"youtube-reviews-and-unboxing-videos.pickle?dl=1"
file_name_pickle = f"youtube-reviews-and-unboxing-videos.pickle?dl=1"

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 1,
}

def unpickle_file(file_name):
    data = pickle.load(open(f'{file_name}', 'rb'))
    data = pd.DataFrame(data).to_parquet()
    return data


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
        bash_command=f'curl -sSLf {url} > {path_to_local_home}/{file_name}'
    )

    unpickle_file_task = PythonOperator(
        task_id="unpickle_file",
        python_callable=unpickle_file,
        op_kwargs={
            "file_name": f"{path_to_local_home}/{file_name_pickle}",
        },
    )
    print_python_version_task = BashOperator(
        task_id="print_python_version",
        bash_command=f'python.__version__()'
    )

if __name__ == '__main__':

    download_dataset_task >> unpickle_file_task >> print_python_version_task