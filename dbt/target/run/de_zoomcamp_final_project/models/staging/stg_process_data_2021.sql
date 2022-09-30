

  create or replace table `de-zoomcamp-artem`.`dbt_ali`.`stg_process_data_2021`
  
  
  OPTIONS()
  as (
    

select 
CountryCode,
Year,
SubmissionYear, 
Category, 
Scenario, 
Gas,
"Final/Gap-filled" as Reported_Value

from `de-zoomcamp-artem`.`final_project_raw_data`.`GHG_projections_2021`
limit 1000
  );
  