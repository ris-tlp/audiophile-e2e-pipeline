WITH iems AS (
    SELECT
        model
    FROM
        public.InEarMonitor
),

FINAL AS (
    SELECT
        iems.model
    FROM
        iems
)

SELECT * FROM FINAL
