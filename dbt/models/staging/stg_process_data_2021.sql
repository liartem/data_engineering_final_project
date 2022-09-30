{{ config(materialized='table') }}

select 
CountryCode,
Year,
SubmissionYear, 
Category, 
Scenario, 
Gas,
Reported_Value

from {{ source('staging', 'GHG_projections_2021') }}
limit 1000