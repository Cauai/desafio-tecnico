from kafka import KafkaProducer
import json
import random
import time



def create_producer():
    return KafkaProducer(
        bootsrap_servers=['localhost:9092'],
        value_serializer=lambda v: json.dumpls(v).encode('utf-8'))

def generate_mock_message(order_id):
    return {
        "order_number": order_id,
        "order_items": [
            {"item_id": i, "qty": random.randint(1, 5), "value_unit": round(random.uniform(10, 500), 2)}
            for i in range(random.randint(1, 5))
        ]
    }

def main():
    producer = create_producer()
    order_id = 1

    while True:
        message = generate_mock_message(order_id)
        producer.send('sales', value=message)
        print(f"Mensagem enviada: {message}")
        order_id += 1
        time.sleep(0.5)  # Envia 1 mensagem a cada meio segundo

if __name__ == "__main__":
    main()
                          