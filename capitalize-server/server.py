# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:42:42 2019

@author: gurjaspal
"""

import socketserver
import threading
#import os
#import csv
from database import Database

d = Database()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    daemon_threads = True
    allow_reuse_address = True

class CapitalizeHandler(socketserver.StreamRequestHandler):
    
#        self.reader = csv.DictReader(self.file)
            
#    def set_value(self, key, value, size= 1024):
#        print('setting value')
#        d.writer.writerow({'key':key, 'value': value, 'size': size})
    
    def handle(self):
        client = f'{self.client_address} on {threading.currentThread().getName()}'
        print(f'Connected: {client}')
        while True:
            data = self.rfile.readline()
            if not data:
                break
            split_data = data.decode('utf-8').split()
            try:
                operation = split_data[0]
                key = split_data[1]
                value = split_data[2]
            except:
                pass
           
            if operation == "set":
                storing_failed = False
                try:
                    d.set_value(key,value)
                except:
                    storing_failed = True
                if storing_failed:
                    self.wfile.write("NOT-STORED\r\n".encode())
                else:
                    self.wfile.write("STORED\r\n".encode())
            elif operation == "get":
                value = d.get_value(key)
                if value:
                    self.wfile.write(value.encode('utf-8'))
                else:
                    self.wfile.write("KEY NOT FOUND\r\n".encode())
            else:
                self.wfile.write("NOT VALID COMMAND\r\n".encode())
#                self.wfile.flush()
        
        
        print(f'Closed: {client}')


#reader = csv.DictReader(file)
        
with ThreadedTCPServer(('', 59899), CapitalizeHandler) as server:
    print(f'The capitalization server is running...')
    server.serve_forever()