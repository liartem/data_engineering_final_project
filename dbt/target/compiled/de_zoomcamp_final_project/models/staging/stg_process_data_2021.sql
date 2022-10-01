

select 
CountryCode,
Year,
SubmissionYear, 
Category, 
Scenario, 
Gas,
cast(`Final_Gap_filled` as numeric) as Reported_Value

from `de-zoomcamp-artem`.`final_project_raw_data`.`GHG_projections_2021`