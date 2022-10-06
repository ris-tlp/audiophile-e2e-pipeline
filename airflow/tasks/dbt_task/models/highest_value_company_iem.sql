WITH company AS (
    SELECT
        *
    FROM
        {{ ref("stg_companynames") }}
),
final AS (
    SELECT
        company.company_name,
        MAX(inearmonitor.value_rating) AS highest_value
    FROM
        company,
        inearmonitor
    WHERE
        company.company_name = {{ dbt.split_part(
            string_text = 'InEarMonitor.model',
            delimiter_text = "' '",
            part_number = 1
        ) }}
    GROUP BY
        company.company_name
)
SELECT
    *
FROM
    final
