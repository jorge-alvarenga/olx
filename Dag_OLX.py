from airflow import DAG
from airflow.utils.dates import days_ago
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.dummy_operator import DummyOperator
from script.olx import web_scraping_OLX,Limpar,subir_banco_de_dados

default_args = {
    "owner":"ilegra",
    "start_date":days_ago(1)
}
with DAG ('Dag_olx', start_date = datetime(2023,1,23), schedule_interval = '@daily',default_args = default_args, catchup = False) as dag:
    inicio = DummyOperator(
        task_id = 'inicio',
    )
    web_scraping_olx = PythonOperator(
        task_id = 'Extrai_web_scraping',
        python_callable = web_scraping_OLX
    )
    tratar= PythonOperator(
        task_id = 'Transforma',
        python_callable = Limpar
    )
    importar_para_banco_de_dados = PythonOperator(
        task_id = 'Carregar',
        python_callable = subir_banco_de_dados
    )
    fim = DummyOperator(
        task_id = 'fim',
    )
inicio>>web_scraping_olx>>tratar>>importar_para_banco_de_dados>>fim