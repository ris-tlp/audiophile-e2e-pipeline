import pathlib
import psycopg2
from dotenv import dotenv_values

# Load config
configuration_path = pathlib.Path(__file__).parent.parent.resolve()
script_path = pathlib.Path(__file__).parent.resolve()
config = dotenv_values(f"{configuration_path}/configuration.env")


def create_conn():
    try:
        conn = psycopg2.connect(
            host=config["rds_instance_endpoint"].split(":")[0],
            port=config["rds_port"],
            user=config["rds_username"],
            password=config["rds_password"],
            dbname=config["rds_database_name"],
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

    # Load from staging to main tables, contains transaction to enable rollbacks
    load_temp_tables_query = prepare_query("load_temp_tables").format(
        bucket_name=config["bucket_name"],
        region=config["aws_region"],
        access_key=config["aws_access_key_id"],
        secret_key=config["aws_secret_access_key"],
    )

    load_main_tables_query = prepare_query("load_main_tables")

    cursor.execute(create_tables_query)
    cursor.execute(load_temp_tables_query)
    cursor.execute(load_main_tables_query)

    conn.commit()
    cursor.close()
    conn.close()
