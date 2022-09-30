{{ config(materialized='table') }}

select * 
except (RY_calibration, Gapfilled)



from {{ source('staging', 'GHG_projections_2019') }}
limit 100