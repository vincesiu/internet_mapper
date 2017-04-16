#!/usr/bin/python3

import pika


if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')



# Change this function to write to a file we open
    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body)

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
