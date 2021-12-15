
SHELL := /usr/local/bin/zsh
AIRFLOW_VERSION=2.2.2
PYTHON_VERSION="$$(python --version | cut -d " " -f 2 | cut -d "." -f 1-2)"
CONSTRAINT_URL="https://raw.githubusercontent.com/apache/airflow/constraints-${AIRFLOW_VERSION}/constraints-${PYTHON_VERSION}.txt"
AIRFLOW_UID=$$(id -u)

create-env:
	python3 -m venv venv
	source venv/bin/activate

airflow-init:
	mkdir -p ./dags ./logs ./plugins
	@echo "AIRFLOW_UID=${AIRFLOW_UID}" > .env
	docker-compose up airflow-init

airflow-start:
	docker-compose up

destroy-env:
	rm -rf ./venv

install-airflow-lib:
	pip install apache-airflow==${AIRFLOW_VERSION} --constraint ${CONSTRAINT_URL}

airflow-stop:
	docker-compose down
	rm -rf ./logs ./.env

clean-up: airflow-stop destroy-env
