#!/usr/bin/python3

import socket

HOST = '0.0.0.0'
PORT = 3000

def connect() :
    global s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True :
        msg = input('\n>>> ')

        if msg == 'q' :
            s.close()
        else :
            s.send(msg.encode())


connect()
