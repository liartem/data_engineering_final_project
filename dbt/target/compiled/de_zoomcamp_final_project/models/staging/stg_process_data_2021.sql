

select 
CountryCode,
Year,
SubmissionYear, 
Category, 
Scenario, 
Gas,
Reported_Value

from `de-zoomcamp-artem`.`final_project_raw_data`.`GHG_projections_2021`
limit 1000