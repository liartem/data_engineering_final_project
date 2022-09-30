{{ config(materialized='table') }}

select 
CountryCode,
Year,
SubmissionYear, 
Category, 
Scenario, 
Gas,
Final/Gap-filled as Reported_Value

from {{ source('staging', 'GHG_projections_2021') }}
limit 1000