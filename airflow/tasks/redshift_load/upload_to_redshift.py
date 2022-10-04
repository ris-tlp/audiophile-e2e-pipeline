import pathlib
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

    # Creating tables
    create_tables_query = prepare_query("create_tables")

    cursor.execute(create_tables_query)
    conn.commit()

