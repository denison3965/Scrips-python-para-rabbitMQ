import pika

def callback(ch, method, properties, body):
    print(" [x] Received %r" % body)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel1 = connection.channel()

channel1.queue_declare(queue='hello')

channel1.basic_consume(queue='hello',
                       auto_ack=True,
                       on_message_callback=callback)

print(' [*] Waiting for messages. To exit press CTRL+C')
channel1.start_consuming()