import pika
import time 

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel1 = connection.channel()

channel1.queue_declare(queue="hello")

messages = ["Primeira mensagem", "Segunda menssagem", "Terceira mensagem", "Quarta mensagem", "Quinta mensagem"];

for message in messages:
    channel1.basic_publish(exchange='',
                           routing_key='hello',
                           body=message)
    print(" [x] Eviada '" + message +"'")
    time.sleep(1)

connection.close()