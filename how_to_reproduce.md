# Create a VM in GCP
It is assumed that the VM instance is created. In order to make the reproduction possible and avoid unexpected bugs, it is reccomended to use the same VM as it was used during the development stage. Based on the platform type, *some* of the steps may be different. It is recomended to refer to [this](https://www.youtube.com/watch?v=ae-CV2KfoN0&list=PL3MmuxUbc_hJed7dXYoJw8DoCuVHhGEQb&index=13&ab_channel=DataTalksClub%E2%AC%9B) video with instructions on setup.


# Terraform (IaC)

before the initializing infrustructure, it is necessary to run:  <br/>
```
gcloud auth application-default login
```
Then it is necessary to cd into *terraform* folder and run following command: 

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
Normally, DAGs are set up to run monthly. It is recommended to run the DAG manually first time.  

# dbt (data build tool) Cloud

1) Create a dbt [account](https://www.getdbt.com/)
2) Create a new project, choose *BigQuery* as a database. For exporting the credentials, export *google_credentials.json* file.
3) Open the project folder in dbt cloud environment, the data transformation may be invoked by command *dbt run*.
**Note:** it is important to choose US location in dbt and BigQuery. Otherwise, dbt will not find the location of BigQuery.  
4) It is possible to choose the automatic transformation of a required data according to provided schedule. For that it is necessary to create new *production* environment, in *trigger* section choose the required schedule.











