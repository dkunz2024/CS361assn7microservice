# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 12:02:41 2022

@author: kunz5
"""

import pika, sys, os

def main():
    
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    channel.queue_declare(queue='hello')

    def callback(ch, method, properties, body):
        print("\nReceived %r" % body)
        print("\nHere are the 5 closest locations to you:")
        print("1234 Super St. Corvallis, OR 97331")
        print("5969 Crazy Frog Ln. Albany, OR 92786")
        print("1279 Ducks-Suck Ave. Eugene, OR 80085")
        print("4464 Parkington Ln. Beaverton, OR 28678")
        print("9034 Beach Dr. Astoria, OR 98254")
    
    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)

    channel.start_consuming()
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)