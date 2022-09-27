# data_engineering_final_project
The final project from data engineering zoomcamp from DataTalksClub

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

Airflow is used as a main orchestrator in this project. In order to run it, it is necessary to go to <code>airflow<code> folder and run following commands: <br/>
1) Build the Airflow Docker image: <br/>

```
docker-compose build
```
2) Initialize the Airflow scheduler, database and so on <br/>

3) Start all services from the containers <br/>

```
docker-compose up airflow-init
```
Then the Airflow can be opened in GUI on [http://localhost:8080/], the username and password are <code>airflow<code> in both cases. <br/>

4) After all work is done, it is necessary to run <br/>
```
docker-compose down
```




