WITH COMPANY AS (
    SELECT
        *
    FROM
        {{ ref("stg_companynames") }}
),

FINAL AS (
    SELECT COMPANY.company_name, MAX(InEarMonitor.value_rating) AS highest_value
    FROM COMPANY, InEarMonitor
    WHERE COMPANY.company_name = {{ dbt.split_part(
            string_text = 'InEarMonitor.model',
            delimiter_text = "' '",
            part_number = 1
        )}}
    GROUP BY COMPANY.company_name
)

SELECT * FROM FINAL
