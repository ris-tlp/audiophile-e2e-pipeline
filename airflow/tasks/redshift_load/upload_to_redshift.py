import pathlib
import psycopg2
from dotenv import dotenv_values
from psycopg2 import sql

# Load config
configuration_path = pathlib.Path(__file__).parent.parent.resolve()
script_path = pathlib.Path(__file__).parent.resolve()
# config = dotenv_values("opt/airflow/tasks/configuration.env")
config = dotenv_values(f"{configuration_path}/configuration.env")


def create_conn(config):
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


def prepare_query(query_filename, *args, **kwargs):
    query_cursor = open(f"{script_path}/queries/{query_filename}.sql", "r")
    query = query_cursor.read()
    query = query.strip()

    # query = sql.SQL(query).format(table_name=sql.Identifier("Headphones"))
    query = query.format(table_name="Headphones")
    print(query)

    return query


if __name__ == "__main__":
    conn = create_conn(config)
    cursor = conn.cursor()
    q = prepare_query("create")

    cursor.execute(q)
    conn.commit()

