# Audiophile End-To-End ELT Pipeline

Pipeline that extracts data from [Crinacle's](https://crinacle.com/) Headphone and InEarMonitor databases and finalizes data for a Metabase Dashboard.

## Architecture

![Architecture](https://github.com/ris-tlp/audiophile-e2e-pipeline/blob/main/images/architecture.jpeg)

Infrastructure provisioning through [Terraform](https://www.terraform.io/), containerized through [Docker](https://www.docker.com/) and orchestrated through [Airflow](https://airflow.apache.org/).

DAG Tasks:

1. Scrape data from [Crinacle's](https://crinacle.com/) website to generate bronze data.
2. Load bronze data to [AWS S3](https://aws.amazon.com/s3/).
3. Initial data parsing and validation through [Pydantic](https://github.com/pydantic/pydantic) to generate silver data.
4. Load silver data to [AWS S3](https://aws.amazon.com/s3/).
5. Load silver data to [AWS Redshift](https://aws.amazon.com/redshift/).
6. Load silver data to [AWS RDS](https://aws.amazon.com/rds/) for future projects.
7. Transform and test data through [dbt](https://docs.getdbt.com/) in the warehouse.
8. Create dashboard through [Metabase](https://www.metabase.com/).

## Dashboard

![Dashboard](https://github.com/ris-tlp/audiophile-e2e-pipeline/blob/main/images/metabase_dashboard.jpeg)

## Requirements

1. Configure AWS account through [AWS CLI](https://aws.amazon.com/cli/). [Reqruired for Terraform]
2. [Terraform](https://www.terraform.io/). [Required to provision AWS services]
3. [Docker / Docker-Compose](https://www.docker.com/). [Required to run Airflow DAG / pipeline]

## Run Pipeline

1. `make infra`: create AWS services. You will be asked to enter a password for your Redshift and RDS clusters.
2. `make config`: generate configuration with Terraform outputs and AWS credentials.
3. `make base-build`: build base airflow image with project requirements.
4. `make build`: build docker images for airflow.
5. `make up`: run the pipeline.
