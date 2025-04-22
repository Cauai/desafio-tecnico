from concurrent.futures import ThreadPoolExecutor
from datetime import datetime



#Essa função recebe uma mensagem no caso dicionário, que representa um pedido de venda.
#Pegar o número do pedido: order_number = message['order_number'].
#Pegar a lista de itens do pedido: items = message['order_items'].
#Calcular o valor total do pedido (qty * value_unit para cada item).
#Salvar a hora do processamento (datetime.utcnow()).


def process_message(message):
    try:
        order_number = message['order_number']
        items = message['order_items']
        total = sum(item['qty'] * item['value_unit'] for item in items)
        processed_at = datetime.utcnow()
        return (order_number, total, processed_at)
    except Exception as e:
        print(f"Erro ao processar mensagem: {message} - {e}")
        return None
    
#Essa função processa um lote de mensagens (batch) e salva os resultados no banco de dados (db_conn).
#Cria um ThreadPoolExecutor com 10 threads permitindo processar varias mensagens ao mesmo tempo paralelamente.
#Cada mensagem é enviada para a função process_message em uma thread separada
#Filtramos os resultados validos e inserimos eles no banco de dados 

def process_batch(batch, db_conn):
    with ThreadPoolExecutor(max_workers=10) as executor:
        results = list(executor.map(process_message, batch))

    valid_results = [r for r in results if r]

    cursor = db_conn.cursor()
    for order_number, total_value, processed_at in valid_results:
        try:
            cursor.execute("""
                INSERT INTO sales (order_number, total_value, processed_at)
                VALUES (%s, %s, %s)
                ON CONFLICT (order_number) DO NOTHING
            """, (order_number, total_value, processed_at))
        except Exception as e:
            print(f"Erro ao salvar no banco: {order_number} - {e}")
            db_conn.rollback()
    db_conn.commit()
    cursor.close()