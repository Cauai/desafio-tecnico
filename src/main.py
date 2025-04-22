from kafka_consumer import create_consumer
from db_connector import connect_db
from processor import process_batch
from psycopg2 import OperationalError

def main():
    db_conn = connect_db()
    consumer = create_consumer()
    batch = []

    for msg in consumer:
        batch.append(msg.value)
        if len(batch) == 100:
            try:
                process_batch(batch, db_conn)
            except OperationalError:
                print("Erro de conexão, tentando reconectar...")
                db_conn = connect_db()
            batch = []

if __name__ == "__main__":
    main()