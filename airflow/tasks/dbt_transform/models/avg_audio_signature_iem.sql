WITH mapped_ranks AS (
    SELECT
        *
    FROM
        {{ ref("stg_maprankvalues") }}
),
final AS (
    SELECT
        inearmonitor.audio_signature,
        AVG(mapped_ranks.rank_value) AS average_rating,
        COUNT(inearmonitor.audio_signature) AS number_of_products
    FROM
        inearmonitor,
        mapped_ranks
    WHERE
        inearmonitor.rank_grade = mapped_ranks.rank_grade
    GROUP BY
        inearmonitor.audio_signature
    HAVING
        COUNT(inearmonitor.audio_signature) > 35
)
SELECT
    *
FROM
    final
