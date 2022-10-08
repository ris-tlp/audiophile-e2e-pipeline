from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.bash_operator import BashOperator
from airflow_dbt.operators.dbt_operator import DbtRunOperator


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
        bash_command="python /opt/airflow/tasks/scraper_extract/scraper.py",
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

    redshift_load = BashOperator(
        task_id="load_data_into_redshift",
        bash_command="python /opt/airflow/tasks/redshift_load/upload_to_redshift.py",
    )

    rds_load = BashOperator(
        task_id="load_data_into_rds",
        bash_command="python /opt/airflow/tasks/rds_load/upload_to_rds.py",
    )

    generate_dbt_profile = BashOperator(
        task_id="generate_dbt_profile",
        bash_command="python /opt/airflow/tasks/dbt_transform/generate_dbt_profile.py"
    )

    dbt_transform = DbtRunOperator(
        task_id="run_dbt_transformations",
        dir="/opt/airflow/tasks/dbt_transform/",
        profiles_dir="/opt/airflow/tasks/dbt_transform"
    )


(
    scrape_audiophile_data
    >> upload_bronze_csv_s3
    >> validate_sanitize_bronze_data
    >> upload_silver_csv_s3
    >> redshift_load
    >> rds_load
    >> generate_dbt_profile
    >> dbt_transform
)
