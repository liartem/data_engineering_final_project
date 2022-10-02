# data_engineering_final_project
`The final project is currently under development. The documentation will be added in some days`

# Demo

![li_artem_data_engineering_demo](https://user-images.githubusercontent.com/54916420/193452868-1c7bdc12-0e71-4faf-9b9f-3b65b41e0df0.gif)


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





