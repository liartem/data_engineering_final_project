

select 
CountryCode,
Year,
SubmissionYear, 
Category_name as Category, 
Scenario, 
Gas,
'Reported Value' as Reported_Value

from `de-zoomcamp-artem`.`final_project_raw_data`.`GHG_projections_2019`
limit 1000