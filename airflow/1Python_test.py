from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime


# ----- 1. Функция, которую будет выполнять PythonOperator -----
def print_hello():
    print("Привет! Это выполняет PythonOperator.")

# ----- 2. Функция, которая принимает контекст -----
def print_context(**context):
    print("Контекст: ", context)
    print("Дата выполнения (ds): ", context["ds"])


# ----- 3. DAG -----
with DAG(
    dag_id="lesson2_python_dag",
    start_date=datetime(2024, 12, 1),
    schedule_interval="@daily",
    catchup=False,
    description="DAG с PythonOperator",
) as dag:
    task_1 = PythonOperator(
        task_id="say_hello",
        python_callable=print_hello,
    )

    task_2 = PythonOperator(
        task_id="show_context",
        python_callable=print_context,
    )

    task_1 >> task_2
