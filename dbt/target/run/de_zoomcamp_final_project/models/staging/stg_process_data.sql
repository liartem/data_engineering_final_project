

  create or replace view `de-zoomcamp-artem`.`dbt_ali`.`stg_process_data`
  OPTIONS()
  as 

select * from `de-zoomcamp-artem`.`final_project_raw_data`.`GHG_projections`
limit 100;

