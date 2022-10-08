-- Each query iterates over the possible rank values for each audio device model and
-- assigns a numerical value to each rank.

{% set rank_grades = ["S+", "S", "S-", "A+", "A", "A-", "B+", "B", "B-", "C+", "C", "C-", "D+", "D", "D-", "E+", "E", "E-", "F+", "F", "F-"] %}
{% set ns = namespace(value=10) %}

WITH iem_ranks AS (
    SELECT DISTINCT
        rank_grade,
        CASE
            {% for grade in rank_grades %}
            WHEN rank_grade = '{{ grade }}' THEN {{ ns.value }}
            {% set ns.value = ns.value + 0.5 %}
            {% endfor %}
        END AS rank_value
    FROM
        inearmonitor
),

{% set ns = namespace(value=10) %}

headphone_ranks AS (
    SELECT DISTINCT
        rank_grade,
        CASE
            {% for grade in rank_grades %}
            WHEN rank_grade = '{{ grade }}' THEN {{ ns.value }}
            {% set ns.value = ns.value + 0.5 %}
            {% endfor %}
        END AS rank_value
    FROM
        headphone
),

final AS (
    SELECT
        rank_grade,
        rank_value
    FROM iem_ranks
    UNION
    SELECT
        rank_grade,
        rank_value
    FROM headphone_ranks
)

SELECT * FROM final
