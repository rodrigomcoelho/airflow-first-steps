from datetime import datetime
from time import sleep

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python import PythonOperator
from utils.date_utils import LOCAL_TZ


def say_something(*args, **kwargs):
    print("Estou dormindo agora")
    sleep(60)
    print(args)


dag = DAG(
    dag_id="demo02",
    default_args={
        "owner": "rodrigo.coelho",
        "start_date": datetime(2021, 12, 1, tzinfo=LOCAL_TZ),
    },
    schedule_interval="@daily",
    tags=["demo", "python", "analytics.engineering"],
)

jobs = {}

jobs["start"] = DummyOperator(task_id="start", dag=dag)
jobs["stop"] = DummyOperator(task_id="stop", dag=dag)
jobs["hello"] = PythonOperator(
    task_id="hello",
    python_callable=say_something,
    op_args="hello",
    dag=dag
)

jobs["hi"] = PythonOperator(task_id="hi", python_callable=say_something, op_args="hello", dag=dag)

jobs["start"].set_downstream(jobs["hello"])

jobs["stop"].set_upstream(jobs["hello"])

jobs["hi"].set_upstream(jobs["start"])  # <<
jobs["hi"].set_downstream(jobs["stop"])  # >>
