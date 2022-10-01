{{ config(materialized='table') }}

select 
CountryCode,
Year,
SubmissionYear, 
Category, 
Scenario, 
Gas,
cast(`Final_Gap_filled` as numeric) as Reported_Value

from {{ source('staging', 'GHG_projections_2021') }}