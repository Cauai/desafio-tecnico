#Responsável por conectar no banco de dados 

import psycopg2
from psycopg2 import OperationalError
import os
import time

MAX_RETRIES = 5
RETRY_DELAY_SECONDS = 5  # Tempo de espera entre tentativas

def connect_db():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'sales_db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASS', 'postgres')
    )


def connect_db():
    attempts = 0
    while attempts < MAX_RETRIES:
        try:
            conn = psycopg2.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                database=os.getenv('DB_NAME', 'sales_db'),
                user=os.getenv('DB_USER', 'postgres'),
                password=os.getenv('DB_PASS', 'postgres')
            )
            print("✅ Conexão com o banco de dados estabelecida com sucesso!")
            return conn
        except OperationalError as e:
            attempts += 1
            print(f"⚠️ Falha ao conectar no banco. Tentativa {attempts}/{MAX_RETRIES}. Erro: {e}")
            time.sleep(RETRY_DELAY_SECONDS)
    # Se falhar todas tentativas
    raise ConnectionError(f"❌ Não foi possível conectar ao banco de dados após {MAX_RETRIES} tentativas.")
