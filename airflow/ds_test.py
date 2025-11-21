"""
Тестовый ДАГ
"""

from datetime import timedelta
import logging

from airflow import DAG
from airflow.utils.dates import days_ago

# Для Airflow 2.x:
from airflow.operators.dummy import DummyOperator
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator

DEFAULT_ARGS = {
    'start_date': days_ago(3),
    'owner': 'Bekhzod',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

with DAG(
    dag_id='bekhzod_test_dag',
    default_args=DEFAULT_ARGS,
    description='Тестовый ДАГ Bekhzod',
    schedule_interval='@daily',
    max_active_runs=1,
    catchup=False,
    tags=['Bekhzod'],
) as dag:

    dummy = DummyOperator(task_id='dummy')

    echo_ds = BashOperator(
        task_id='echo_ds',
        bash_command='echo {{ ds }}'
    )

    def hello_world_func(**kwargs):
        logging.info('Hello World')

    hello_world = PythonOperator(
        task_id='hello_world',
        python_callable=hello_world_func
    )

    dummy >> echo_ds >> hello_world
