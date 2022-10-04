# cd /opt/terraform/
# touch /opt/airflow/tasks/configuration.env
# terraform output >> /opt/airflow/tasks/configuration.env
# cat /opt/airflow/tasks/configuration.envs

touch #airflow/tasks/configuration.env
cd terraform/
terraform output > ../airflow/tasks/configuration.env
