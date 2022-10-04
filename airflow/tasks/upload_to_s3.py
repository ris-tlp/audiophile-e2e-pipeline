import sys
import boto3
import pathlib
from dotenv import dotenv_values
from botocore.exceptions import ClientError, NoCredentialsError

# Load config
script_path = pathlib.Path(__file__).parent.resolve()
config = dotenv_values(f"{script_path}/configuration.env")

# Get CLI arg for data phase upload, ie, bronze, silver, gold
data_level = sys.argv[1]
files = [f"headphones-{data_level}.csv", f"iems-{data_level}.csv"]

# Set config variables
AWS_BUCKET = config["bucket_name"]


def connect_s3():
    """
    Create a boto3 session and connect to the S3 Resource

    Returns:
        connection to the S3 bucket
    """
    try:
        s3_conn = boto3.resource("s3")
        return s3_conn
    except NoCredentialsError as e:
        raise (e)


def upload_csv_s3():
    """
    Upload both CSV files to the S3 bucket
    """
    s3_conn = connect_s3()
    for file in files:
        s3_conn.meta.client.upload_file(Filename=f"/tmp/{file}", Bucket=AWS_BUCKET, Key=file)


if __name__ == "__main__":
    upload_csv_s3()
