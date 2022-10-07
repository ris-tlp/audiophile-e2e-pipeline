-- Each query iterates over the possible rank values for each audio device model and
-- assigns a numerical value to each rank.

{% set rank_grades = ["S+", "S", "S-", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E+", "E", "E-", "F+", "F", "F-"] %}
{% set value = 10 %}

WITH iem_ranks as (
    SELECT
        DISTINCT rank_grade,
        CASE
        {% for grade in rank_grades %}
         WHEN rank_grade = '{{ grade }}' THEN {{ value }}
        {% set value = value - 0.5 %}
        {% endfor %}
        END rank_value
    FROM
        InEarMonitor
),

{% set value = 10 %}

headphone_ranks as (
    SELECT
        DISTINCT rank_grade,
        CASE
        {% for grade in rank_grades %}
         WHEN rank_grade = '{{ grade }}' THEN {{ value }}
        {% set value = value - 0.5 %}
        {% endfor %}
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
