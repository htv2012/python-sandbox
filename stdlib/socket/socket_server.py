#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 17:07:56 2013

@author: haiv

Socket server

"""
import socket


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = ''
s.bind((host, port))
print(('waiting for connection on port', port))

s.listen(5)
counter = 1
while True:
    client_socket, address = s.accept()
    print(('ACCEPT:', client_socket, address))
    client_socket.send(str(counter) + '\r\n')
    client_socket.close()
