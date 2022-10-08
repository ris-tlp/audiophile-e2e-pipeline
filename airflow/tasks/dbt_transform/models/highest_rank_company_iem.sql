WITH mapped_ranks AS (
    SELECT
        *
    FROM
        {{ ref("stg_maprankvalues") }}
),
company AS (
    SELECT
        *
    FROM
        {{ ref("stg_companynames") }}
),
final AS (
    SELECT
        company.company_name,
        AVG(mapped_ranks.rank_value) AS average_rating,
        COUNT(company.company_name) AS number_of_products
    FROM
        inearmonitor,
        mapped_ranks,
        company
    WHERE
        inearmonitor.rank_grade = mapped_ranks.rank_grade
        AND company.company_name = {{ dbt.split_part(
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
