WITH iem_ranks as (
    SELECT DISTINCT rank_grade,
    CASE
        WHEN rank_grade = 'S+' THEN 10
        WHEN rank_grade = 'S' THEN 9.5
        WHEN rank_grade = 'S-' THEN 9
        WHEN rank_grade = 'A+' THEN 8.5
        WHEN rank_grade = 'A' THEN 8
        WHEN rank_grade = 'A-' THEN 7.5
        WHEN rank_grade = 'B+' THEN 7
        WHEN rank_grade = 'B' THEN 6.5
        WHEN rank_grade = 'B-' THEN 6
        WHEN rank_grade = 'C+' THEN 5.5
        WHEN rank_grade = 'C' THEN 5
        WHEN rank_grade = 'C-' THEN 4.5
        WHEN rank_grade = 'D+' THEN 4
        WHEN rank_grade = 'D' THEN 3.5
        WHEN rank_grade = 'D-' THEN 3
        WHEN rank_grade = 'E+' THEN 2.5
        WHEN rank_grade = 'E' THEN 2
        WHEN rank_grade = 'E-' THEN 1.5
        WHEN rank_grade = 'F+' THEN 1
        WHEN rank_grade = 'F' THEN 0.5
        WHEN rank_grade = 'F-' THEN 0
    END rank_value
    FROM InEarMonitor
),
headphone_ranks as (
    SELECT
        DISTINCT rank_grade,
        CASE
            WHEN rank_grade = 'S+' THEN 10
            WHEN rank_grade = 'S' THEN 9.5
            WHEN rank_grade = 'S-' THEN 9
            WHEN rank_grade = 'A+' THEN 8.5
            WHEN rank_grade = 'A' THEN 8
            WHEN rank_grade = 'A-' THEN 7.5
            WHEN rank_grade = 'B+' THEN 7
            WHEN rank_grade = 'B' THEN 6.5
            WHEN rank_grade = 'B-' THEN 6
            WHEN rank_grade = 'C+' THEN 5.5
            WHEN rank_grade = 'C' THEN 5
            WHEN rank_grade = 'C-' THEN 4.5
            WHEN rank_grade = 'D+' THEN 4
            WHEN rank_grade = 'D' THEN 3.5
            WHEN rank_grade = 'D-' THEN 3
            WHEN rank_grade = 'E+' THEN 2.5
            WHEN rank_grade = 'E' THEN 2
            WHEN rank_grade = 'E-' THEN 1.5
            WHEN rank_grade = 'F+' THEN 1
            WHEN rank_grade = 'F' THEN 0.5
            WHEN rank_grade = 'F-' THEN 0
        END rank_value
    FROM
        Headphone
),

final AS (
    SELECT rank_grade, rank_value FROM iem_ranks
    UNION
    SELECT rank_grade, rank_value FROM headphone_ranks
)

SELECT * FROM final
