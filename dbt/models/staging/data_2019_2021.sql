/*{{ config(materialized='table') }}
with data_2021 as (
    select *
    from {{ source('staging', 'GHG_projections_2021') }}
), 

data_2019 as (
    select *
    from {{ source('staging', 'GHG_projections_2021') }}
)

select 
    CountryCode,
    /*data_2021.CountryCode,*/
    /*Year, 
    /*data_2021.Year,*/
    /*sum(Reported_Value) as Reported_value_2019,
 /*   data_2021.Final_Gap_filled as Reported_value_2021*/

/*from data_2019
/*inner join data_2021
on data_2019.CountryCode = data_2021.CountryCode and data_2019.Year = data_2021.Year*/
