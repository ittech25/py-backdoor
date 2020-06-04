#!/usr/bin/python3

import socket

HOST = '0.0.0.0'
PORT = 3000

""" Open a TCP server socket """
def create_socket() :
    global s 

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen(5)

    print(f'Server launched :: {HOST}:{PORT}')

    while True :
        data = s.recv(50)
        print(data)
        if not data :
            break

    s.close()

create_socket()
