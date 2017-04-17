#!/usr/bin/python3

import pickle
import pika




# Change this function to write to a file we open
def callback(ch, method, properties, pickle_dic):
    print(" [x] Received something")

    dic = pickle.loads(pickle_dic, fix_imports = True, encoding = 'ASCII', errors = 'strict')
    write_data(dic)


def write_data(dic):
    file_object = open('log_' + dic['host_url'] + '.txt', 'a')
    file_object.write(dic['target_url'] + ',' + dic['digest'] + ',' + dic['response_time'] + '\n')
    file_object.close() 



if __name__ == '__main__':
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.queue_declare(queue='hello')

    channel.basic_consume(callback,
                          queue='hello',
                          no_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()
