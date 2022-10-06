WITH final AS (
    SELECT
        *
    FROM
        {{ ref("stg_maprankvalues") }}
)

SELECT * FROM final
