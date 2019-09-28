# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 16:47:17 2019

@author: gurjaspal
"""
import socket
ip = '127.0.0.1'
port  = 9889
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect((ip, port))
    
    sock.sendall(bytes(message, 'ascii'))
    response = str(sock.recv(1024), 'ascii')
    print("Received: {}".format(response))