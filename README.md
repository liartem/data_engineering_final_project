

# Problem description
The project analyzed the *projected* Green House Gases (GHG) emission of EU member states from 2 given time periods (2019 and 2021). The EU countries are obligated to report its GHG projections ‘with existing measures’ scenario. The project compares the results of 2 projections and provide valuable insights. <br/> 
This project has been done as part of **data engineering zoomcamp** from [DataTalksClub](https://github.com/DataTalksClub/data-engineering-zoomcamp) completed in *self-paced* mode. 


# Technical overview
![datsystem_design_data_engineering_li_artem](https://user-images.githubusercontent.com/54916420/193460925-5458dc6b-968a-43e9-bfcf-b303552bf6d9.jpg)

The service is operated ib the [GCP](https://cloud.google.com/) cloud virtual machine. The infrustructure is managed by [Terraform](https://www.terraform.io/). 
The created service **extract** the data from external data [source](https://data.europa.eu/data/datasets/dat-2-en?locale=en) for 2019 and 2021 reported years *(download_dataset_task, unzip_data_file_task, convert_to_parquet_task)*, **load** the data to google cloud [storage](https://cloud.google.com/storage) *(upload_to_gcs_task, bigquery_exernal_table_task)* , connects [BigQuery](https://cloud.google.com/bigquery), **transform** (make the structure for data with) [dbt](https://www.getdbt.com/) and builds [dashboards](https://datastudio.google.com/reporting/b71a8a3a-481d-4c66-8729-ebbe82c71abe) with Google Data [Studio](https://datastudio.google.com/u/0/).

All pipelines are orchestrated with help of Apache [Airflow](https://airflow.apache.org/), which starts from [Docker](https://www.docker.com/).


# Demo
The projected demo presents the visualization step - the final stage of the whole pipeline.
The final results also available **[here](https://datastudio.google.com/reporting/b71a8a3a-481d-4c66-8729-ebbe82c71abe)**
![li_artem_data_engineering_demo](https://user-images.githubusercontent.com/54916420/193453147-1cacfab5-c31d-4792-9aa3-6193c61f9a60.gif)

# Possibility for improvements and bugs
1) The biggest bug is connected to the discrepancies in Airflow Dag: the picture below indicates the results of running the same Dag **without** any change multiple times. It can be seen that sometimes the execution results are positive, sometimes the same pipeline produces a mistake in some tasks. Up to now, the reason for that is not defined.
![577bf57e1f767e748eb52f21645fe117](https://user-images.githubusercontent.com/54916420/193528619-3ba28ec2-9907-4840-bb8b-9498e9be5650.png)

2) Overall it is possible to add another external data for the analysis: for example add the population of countries and compare the projected emission per person (but is it still difficult to predict the population of countries in future).

3) It is possible to add the other years for the analysis and make extraction DAG (script) more parametrized. However, since the nature of web and absence of required structure for the report, it may seems as the most difficult task.

4) Add CI/CD pipeline. 

# Terraform (IaC)

before the initializing infrustructure, it is necessary to run:  <br/>
```
gcloud auth application-default login
```
### Initialize state file (.tfstate)
```
terraform init
```
### Check changes to new infra plan
```
terraform plan 
```
### Create new infra
```
terraform apply 
```
### Delete infrastructure
```
terraform destroy
```
# Airflow (Orchestrator)

Airflow is used as a main orchestrator in this project. In order to run it, it is necessary to go to `airflow` folder and run following commands: <br/>
1) Build the Airflow Docker image: <br/>
```
docker-compose build
```
2) Initialize the Airflow scheduler, database and so on <br/>
```
docker-compose up airflow-init
```
3) Start all services from the containers <br/>
```
docker-compose up
```
Then the Airflow can be opened in GUI on [http://localhost:8080/](http://localhost:8080/), the username and password are **airflow** in both cases. <br/>

4) After all work is done, it is necessary to run <br/>
```
docker-compose down
```





