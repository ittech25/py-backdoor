#!/usr/bin/python3

import socket

HOST = '0.0.0.0'
PORT = 3000

def connect() :
    global s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True :
        data = s.recv(4028)
        print(data)


connect()
