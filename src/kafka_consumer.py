# Função para criar e configurar o consumidor Kafka

from kafka import KafkaConsumer
import json

def create_consumer():
    return KafkaConsumer(
        'sales',                                         #Aqui estamos escutando o tópico Sales.
        bootstrap_servers=['localhost:9092'],            #Define onde o kafka está rodando (neste caso localmente na porta 9092).
        auto_offset_reset='earliest',                    #Se o consumidor não tiver uma posição salva (offset), ele começará a consumir desde o início (earliest)
        enable_auto_commit=True,                         #True --> o Kafka sabe até onde parou a leitura.
        group_id='sales-group',                          #Define o grupo de consumidores, sendo vários consumidores no mesmo group_id compartilhando a carga de trabalho(consumo das mensagens)
        value_deserializer=lambda x: json.loads(x.decode('utf-8'))
    )
