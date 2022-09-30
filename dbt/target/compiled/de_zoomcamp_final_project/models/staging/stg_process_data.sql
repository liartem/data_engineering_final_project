

select * 
except (RY_calibration, Gapfilled)



from `de-zoomcamp-artem`.`final_project_raw_data`.`GHG_projections_2019`
limit 100