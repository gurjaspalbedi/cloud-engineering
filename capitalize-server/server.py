# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 17:42:42 2019

@author: Jassi
"""
#REFERENCES
#https://realpython.com/python-csv/
#https://realpython.com/python-sockets/
#https://cs.lmu.edu/~ray/notes/pythonnetexamples/
#https://realpython.com/read-write-files-python/
#https://realpython.com/python-sockets/

import socketserver
import threading
from database import Database

d = Database()


class ThreadedTCPServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    # Threaded TCP to server multiple clients and for concurrency
    
    daemon_threads = True
    allow_reuse_address = True

class KeyValueHandler(socketserver.StreamRequestHandler):
    # Overriding the handle funtion
    # When this method is finished wfile gets flushed by itself
    
    def handle(self):
        thread = threading.current_thread().getName()
        print(f'Client connected on thread:' + thread)
        while True:
            data = self.rfile.next()
            
            # this will only be empty if the client disconnects, empty string will also be appended with '\n'
            # hence this would work even if the client sends the empty string
            # it breaks the loop if client disconnects
            if not data:
                break
            split_data = data.decode('utf-8').split()
            try:
                operation = split_data[0]
                key = split_data[1]
                value = split_data[2]
            except:
                self.wfile.write("COMMAND FORMAT NOT CORRECT, <Operation> <key> <value>? \r\n".encode())
           
            if operation == "set":
                # SET OPERATION
                # Assuming that the operation will not fail
                storing_failed = False
                try:
                    d.set_value(key,value)
                except:
                    # Operation failed
                    storing_failed = True
                if storing_failed:
                    # Message when operation failed
                    self.wfile.write("NOT-STORED\r\n".encode())
                else:
                    # Message when operation is successful
                    self.wfile.write("STORED\r\n".encode())
                # Get operation
            elif operation == "get":
                value = d.get_value(key)
                if value:
                    # returning the value if it exist
                    self.wfile.write(value.encode('utf-8'))
                else:
                    # Case when key not found
                    self.wfile.write("KEY NOT FOUND\r\n".encode())
            else:
                # if operation is not set or get
                self.wfile.write("NOT VALID COMMAND\r\n".encode())
        
        print("Client closed on thread" + thread)
        
with ThreadedTCPServer(('localhost', 9899), KeyValueHandler) as server:
    print('Waiting for the clients')
    server.serve_forever()