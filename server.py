import socket
import sys

## create socket
def create_socket():
    global host
    global port 
    global s
    
    host = ''
    port = 10000

    try :
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print('Socket created')
    except socket.error as err :
        print('Error Creation Socket :', err)
        create_socket()

## Binding the socket 
def bind_socket():
    global host
    global port
    global s

    try :
        s.bind( (host, port) )
        s.listen(5)
        print('Socket bounded')
    except socket.error as err:
        print('Socket Binding error :', err)
        bind_socket()

## accepting client 
def accept():
    global s

    client, address = s.accept()
    print('Connection ESTABLISH ', address[0], 'PORT', address[1])
    send_commands(client)
    client.close()

## Send Commands
def send_commands(client):
    global s

    while True :
        cmd = input('>>>')
        if cmd == 'quit' :
            client.close()
            s.close()
            sys.exit()
        elif len(cmd) > 0:
            client.send(str.encode(cmd))
            data = str(client.recv(1024))
            print(data, end="")


def main() :
    create_socket()
    bind_socket()
    accept()

if __name__== '__main__' :
    try :  
        main()
    except KeyboardInterrupt:
        sys.exit()



















































