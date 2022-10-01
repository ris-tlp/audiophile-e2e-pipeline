FROM apache/airflow:2.4.1

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
    build-essential \
    && apt-get autoremove -yqq --purge \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

USER airflow

COPY /Pipfile /Pipfile
COPY /Pipfile.lock /Pipfile.lock

# Dependencies
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv requirements > requirements.txt
RUN pip install --no-cache-dir --user -r requirements.txt
