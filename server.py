#!/usr/bin/python3

import socket, sys
from queue import Queue

HOST = '0.0.0.0'
PORT = 3000

address_list = []
connections_list = []

q = Queue()


""" Open a TCP server socket """
def create_socket() :
    global objSocket

    try :
        objSocket = socket.socket()
        objSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    except socket.error() as ex :
        print(f'Error creating Socket :{str(ex)}\n')

""" Binding SOCKET """
def bind_socket() :
    while :
        try :
            objSocket.bind((HOST, PORT))
            objSocket.listen(20)
            print(f'Socket Created on {HOST}:{PORT}\n')
            break()
        except socket.error() as ex:
            print(f'error Binding Socket {ex}\n')

""" Accept incomming connections """
def accept_connections() :
    while True :
        conn, addr = s.accept()
        connections_list.append(conn)

