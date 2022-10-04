from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator


schedule_interval = "@daily"
start_date = days_ago(1)
default_args = {"owner": "airflow", "depends_on_past": False, "retries": 1}

with DAG(
    dag_id="audiophile_e2e_pipeline",
    schedule_interval=schedule_interval,
    default_args=default_args,
    start_date=start_date,
    catchup=True,
    max_active_runs=1,
) as dag:

    scrape_audiophile_data = BashOperator(
        task_id="scrape_audiophile_data",
        bash_command="python /opt/airflow/tasks/scraper/scraper.py",
    )

    upload_bronze_csv_s3 = BashOperator(
        task_id="upload_bronze_csv_to_s3",
        bash_command="python /opt/airflow/tasks/upload_to_s3.py bronze",
    )

    validate_sanitize_bronze_data = BashOperator(
        task_id="validate_sanitize_bronze_data",
        bash_command="python /opt/airflow/tasks/validate_sanitize_bronze.py",
    )

    upload_silver_csv_s3 = BashOperator(
        task_id="upload_silver_csv_to_s3",
        bash_command="python /opt/airflow/tasks/upload_to_s3.py silver",
    )
(
    scrape_audiophile_data
    >> upload_bronze_csv_s3
    >> validate_sanitize_bronze_data
    >> upload_silver_csv_s3
)
