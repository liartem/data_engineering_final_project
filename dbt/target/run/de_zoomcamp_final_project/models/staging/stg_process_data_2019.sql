

  create or replace table `de-zoomcamp-artem`.`dbt_ali`.`stg_process_data_2019`
  
  
  OPTIONS()
  as (
    

select 
CountryCode,
Year,
SubmissionYear, 
Category_name as Category, 
Scenario, 
Gas,
Reported_Value



from `de-zoomcamp-artem`.`final_project_raw_data`.`GHG_projections_2019`
limit 1000
  );
  