import os
import logging

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

from airflow.providers.google.cloud.operators.bigquery import BigQueryCreateExternalTableOperator, BigQueryInsertJobOperator

from datetime import datetime
from zipfile import ZipFile
import zipfile

from google.cloud import storage

import pandas as pd
from glom import glom
import json
import gzip
import pickle
import pyarrow.parquet as pq
import pyarrow.csv as pv


path_to_local_home = os.environ.get("AIRFLOW_HOME", "/opt/airflow/")
url = f"https://www.eea.europa.eu/data-and-maps/data/greenhouse-gas-emission-projections-for-8/2021-preliminary-ghg-projections-reported/ghg_projections_2021_preliminary_csv/at_download/file"
file_name_zip = f"GHG_projections_2021_EEA.zip"
file_name_csv = f"GHG_projections_2021_EEA.csv"

parquet_file = f"GHG_projections_2021_EEA.parquet"

PROJECT_ID = os.environ.get("GCP_PROJECT_ID")
BUCKET = os.environ.get("GCP_GCS_BUCKET")
BIGQUERY_DATASET = 'final_project_raw_data'

default_args = {
    "owner": "airflow",
    "depends_on_past": False,
    "retries": 0,
}

def extract_from_zip(path_to_file):
    with ZipFile(f'{path_to_file}', 'r') as zipObj:
        zipObj.extract(path_to_file)


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


def unzip_data_file(path_to_zip_file, directory_to_extract_to):
    with ZipFile(path_to_zip_file, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)


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
        bash_command=f'curl -sSLf {url} > {path_to_local_home}/{file_name_zip}'
    )

    print_output_task = BashOperator(
        task_id="print_output_task",
        bash_command=f'cd {path_to_local_home} && ls'
    )

    unzip_data_file_task = PythonOperator(
        task_id = "unzip_data_file_task",
        python_callable=unzip_data_file,
        op_kwargs={
            "path_to_zip_file": f"{path_to_local_home}/{file_name_zip}",
            "directory_to_extract_to": f"{path_to_local_home}",
        },
    )

    convert_to_parquet_task = PythonOperator(
        task_id="convert_to_parquet_task",
        python_callable=convert_to_parquet,
        op_kwargs={
            "file_name": f"{path_to_local_home}/{file_name_csv}",
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

    bigquery_external_table_task = BigQueryCreateExternalTableOperator(
        task_id="bigquery_external_table_task",
        table_resource={
            "tableReference": {
                "projectId": PROJECT_ID,
                "datasetId": BIGQUERY_DATASET,
                "tableId": "GHG_projections",
            },

            "externalDataConfiguration": {
                "sourceFormat": "PARQUET",
                "sourceUris": [f"gs://{BUCKET}/raw/{parquet_file}"],
            },
        },
    )

if __name__ == '__main__':

    download_dataset_task >> print_output_task >> unzip_data_file_task >> convert_to_parquet_task >> upload_to_gcs_task >> bigquery_external_table_task