WITH mapped_ranks AS (
    SELECT
        *
    FROM
        {{ ref("stg_maprankvalues") }}
),
final AS (
    SELECT
        headphone.audio_signature,
        AVG(mapped_ranks.rank_value) AS average_rating,
        COUNT(headphone.audio_signature) AS number_of_products
    FROM
        headphone,
        mapped_ranks
    WHERE
        headphone.rank_grade = mapped_ranks.rank_grade
    GROUP BY
        headphone.audio_signature
    HAVING
        COUNT(headphone.audio_signature) > 15
)
SELECT
    *
FROM
    final
