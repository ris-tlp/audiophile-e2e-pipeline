cd terraform/
terraform output > ../airflow/tasks/configuration.env
cat $HOME/.aws/credentials >> ../airflow/tasks/configuration.env
