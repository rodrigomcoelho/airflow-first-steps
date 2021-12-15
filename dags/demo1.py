from datetime import datetime

from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from airflow.sensors.external_task_sensor import ExternalTaskSensor
from utils.date_utils import LOCAL_TZ


def foo():
    print("Agora foi!")

with DAG(
    dag_id="demo01",
    default_args={
        "owner": "rodrigo.coelho",
        "start_date": datetime(2021, 11, 28, tzinfo=LOCAL_TZ),
    },
    schedule_interval="@daily",
    tags=["demo", "python", "analytics.engineering"],
) as dag:

    operator_sensor = ExternalTaskSensor(
        task_id="sensor",
        external_dag_id="demo02",
        external_task_id="hello",
        poke_interval=10, # verifica se a task foi finalizada a cada X segundos
        timeout=120, # se a task não finalizar em X segundos, cancela a task
    )

    operator_start = DummyOperator(task_id="start")
    operator_foo = PythonOperator(task_id="foo", python_callable=foo, dag=dag)
    operator_stop = DummyOperator(task_id="stop", dag=dag)

    operator_start >> operator_sensor >> operator_foo >> operator_stop
