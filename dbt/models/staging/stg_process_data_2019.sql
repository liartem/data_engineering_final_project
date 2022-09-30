{{ config(materialized='table') }}

select 
CountryCode,
Year,
SubmissionYear, 
Category_name as Category, 
Scenario, 
Gas,
Reported Value



from {{ source('staging', 'GHG_projections_2019') }}
limit 1000