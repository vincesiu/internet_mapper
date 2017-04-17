#!/usr/bin/python3

import hashlib
import pika
import time
import requests
import pickle

from random import choice


def get_info(input_url):

    resp = requests.get(input_url, timeout = 0.25)
    ret = {}

    
    if resp.status_code is not 200:
        return None

    m = hashlib.sha256()
    m.update(resp.content)

    ret['digest'] = m.hexdigest()
    ret['host_url'] = choice(['192.168.0.1', '10.0.0.4', '333.524.1.8'])
    ret['target_url'] = resp.url
    ret['response_time'] = str(resp.elapsed)

    resp.close()


    
    return ret


#def get_info_range(ip_min, ip_max):
#   for(
    

if __name__ == '__main__':

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()


    channel.queue_declare(queue='hello')

    test_dict = get_info('https://www.google.com')
    test_ip = get_info('http://74.125.21.104')

    pickled_dict = pickle.dumps(test_ip, pickle.HIGHEST_PROTOCOL)
    
    google_ips = ['74.125.21.147', '74.125.21.105', '74.125.21.103', '74.125.21.106', '74.125.21.99', '74.125.21.104']

    

    # Check if IP address is not black hole
    channel.basic_publish(exchange='',
                          routing_key='hello',
                          body=pickled_dict)


    print(" [x] Sent message")
    connection.close()

#print(repr(get_info('https://www.google.com')))
