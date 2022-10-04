import pathlib
from tempfile import tempdir
import psycopg2
from psycopg2 import sql
from dotenv import dotenv_values

# Load config
configuration_path = pathlib.Path(__file__).parent.parent.resolve()
script_path = pathlib.Path(__file__).parent.resolve()
config = dotenv_values(f"{configuration_path}/configuration.env")


def create_conn():
    try:
        conn = psycopg2.connect(
            host=config["redshift_host"].split(":")[0],
            port=config["redshift_port"],
            user=config["redshift_user"],
            password=config["redshift_password"],
            dbname=config["redshift_database"],
        )

        return conn
    except Exception as exception:
        print(exception)


def prepare_query(query_filename: str) -> str:
    """
    Helper method to concatenate entire query and help with preparing parameters

    Args:
        query_filename (str): name of the sql file containing query

    Returns:
        str: completely concatenated query
    """
    query_cursor = open(f"{script_path}/queries/{query_filename}.sql", "r")
    query = query_cursor.read()

    return query


if __name__ == "__main__":
    conn = create_conn()
    cursor = conn.cursor()

    # Creating tables if not already created
    create_tables_query = prepare_query("create_tables")

    #
    temp_load_query = prepare_query("load_csv_temp")
    temp_load_query = temp_load_query.format(
        s3_iems_file=f"https://{config['bucket_name']}.s3.amazonaws.com/iems-silver.csv",
        s3_headphones_file=f"https://{config['bucket_name']}.s3.amazonaws.com/headphones-silver.csv",
        aws_access_id=config["aws_access_key_id"],
        aws_secret_key=config["aws_secret_access_key"]
    )
    cursor.execute(create_tables_query)

    print(temp_load_query)
    cursor.execute(temp_load_query)
    conn.commit()
