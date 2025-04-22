#Responsável por conectar no banco de dados 

import psycopg2
from psycopg2 import OperationalError
import os

def connect_db():
    return psycopg2.connect(
        host=os.getenv('DB_HOST', 'localhost'),
        database=os.getenv('DB_NAME', 'sales_db'),
        user=os.getenv('DB_USER', 'postgres'),
        password=os.getenv('DB_PASS', 'postgres')
    )