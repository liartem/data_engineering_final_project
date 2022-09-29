{{ config(materialized='view') }}

select * 




from {{ source('staging', 'GHG_projections') }}
limit 100