WITH mapped_ranks AS (
    SELECT
        *
    FROM
        {{ ref("stg_maprankvalues") }}
),
final AS (
    SELECT
        headphone.driver_type,
        AVG(mapped_ranks.rank_value) AS average_rating,
        COUNT(headphone.driver_type) AS number_of_products
    FROM
        headphone,
        mapped_ranks
    WHERE
        headphone.rank_grade = mapped_ranks.rank_grade
    GROUP BY
        headphone.driver_type
)
SELECT
    *
FROM
    final
