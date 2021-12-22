import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='log', exchange_type='fanout')

messages = ["Primeiro log", "Segundo log", "Terceiro log", "Quarto log", "Quinto log"];

for mensage in messages:
    channel.basic_publish(exchange='logs',
                          routing_key='',
                          body=mensage)
    print(" [x] Enviada '" + mensage + "'")
    time.sleep(1)

connection.close()