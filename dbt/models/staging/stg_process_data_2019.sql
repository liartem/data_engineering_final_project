{{ config(materialized='table') }}

select 
CountryCode,
Year,
SubmissionYear, 
Category_name as Category, 
Scenario, 
Gas,
cast(`Reported_Value` as numeric) as Reported_Value

from {{ source('staging', 'GHG_projections_2019') }}
limit 100