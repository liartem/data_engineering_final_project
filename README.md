# data_engineering_final_project
The final project from data engineering zoomcamp from DataTalksClub

<h1> Terraform (IaC) <h1>

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

### Delete infra after your work, to avoid costs on any running services
```
terraform destroy
```
