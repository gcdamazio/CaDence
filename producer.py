from time import sleep
from json import dumps
from kafka import KafkaProducer


producer = KafkaProducer(bootstrap_servers=['localhost:9092'],value_serializer=lambda x: dumps(x).encode('utf-8'))


for e in range(10000):
    data = {'number': e}  
    producer.send('testtopic', value=data)  
    sleep(2)


producer.flush()
producer.close()
