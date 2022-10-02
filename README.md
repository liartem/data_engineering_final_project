# Problem description
The project analyzed the *projected* Green House Gases (GHG) emission of EU member states from 2 given time periods (2019 and 2021). The EU countries are obligated to report its GHG projections ‘with existing measures’ scenario  <br/> 
This project has been done as part of data angineering zoomcamp from [DataTalksClub](https://github.com/DataTalksClub/data-engineering-zoomcamp) completed in *self-paced* mode. 


# Technical overview
The service is operated ib the [GCP](https://cloud.google.com/) cloud virtual machine. The infrustructure is managed by [Terraform](https://www.terraform.io/). 
The created service **extract** the data from external data [source](https://data.europa.eu/data/datasets/dat-2-en?locale=en) for 2019 and 2021 reported years, **load** the data to google cloud [storage](https://cloud.google.com/storage), connects [BigQuery](https://cloud.google.com/bigquery), **transform** (make the structure for data with) [dbt](https://www.getdbt.com/) and builds [dashboards](https://datastudio.google.com/reporting/b71a8a3a-481d-4c66-8729-ebbe82c71abe) with Google Data [Studio](https://datastudio.google.com/u/0/).

All pipelines are orchestrated with help of Apache [Airflow](https://airflow.apache.org/), which starts from [Docker](https://www.docker.com/).

# Demo

![li_artem_data_engineering_demo](https://user-images.githubusercontent.com/54916420/193453147-1cacfab5-c31d-4792-9aa3-6193c61f9a60.gif)


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





