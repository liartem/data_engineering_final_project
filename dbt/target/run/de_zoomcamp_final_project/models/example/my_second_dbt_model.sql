

  create or replace view `de-zoomcamp-artem`.`dbt_ali`.`my_second_dbt_model`
  OPTIONS()
  as -- Use the `ref` function to select from other models

select *
from `de-zoomcamp-artem`.`dbt_ali`.`my_first_dbt_model`
where id = 1;

