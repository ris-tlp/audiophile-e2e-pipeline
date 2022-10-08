help:
	@echo "  build      Builds the docker images for the docker-compose setup"
	@echo "  clean       Stops and removes all docker containers"
	@echo "  shell       Opens a Bash shell"
	@echo "  redis-cli   Opens a Redis CLI"
	@echo "  run         Run a airflow command"
	@echo "  stop        Stops the docker containers"
	@echo "  up          Runs the whole stack, served under http://localhost:8080/"
	@echo "  init        Initializes airflow services"
	@echo "  base-build  Builds the base docker image for airflow"
	@echo "  test  		 UI tests for scraper"
	@echo "  config      Generate a configuration using terraform outputs"
	@echo "  test-dbt    Run tests for dbt build"

build:
	docker-compose build

clean:	stop
	docker-compose rm -f
	rm -rf logs/*
	if [ -f airflow-worker.pid ]; then rm airflow-worker.pid; fi

shell:
	docker-compose run web bash

redis-cli:
	docker-compose run redis redis-cli -h redis

run:
	docker-compose run -v ~/.aws/:/root/.aws web airflow $(COMMAND)

stop:
	docker-compose down
	docker-compose stop

up:
	docker-compose up

init:
	docker-compose up airflow-init

base-build:
	docker build -t airflow-extended:latest -f Dockerfile .

test-scraper:
	pytest

test-dbt:
	dbt test

config:
	chmod +x generate_config.sh
	./generate_config.sh

infra:
	terraform -chdir=terraform/ init -input=false
	terraform -chdir=terraform/ apply


