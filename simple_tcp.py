#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 简单的tcp服务器和客户端

import socket,argparse

def recvall(sock,length):
    data = b''
    while len(data) < length:
        more = sock.recv(length-len(data))
        if not more:
            raise EOFError('was expecting %d bytes but only received %d bytes before the socket closed' % (length,len(data)))
        data += more

    return data

def server(interface,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
    sock.bind((interface,port))
    sock.listen(1)
    print('listening at ',sock.getsockname())

    while True:
        sc,sockname = sock.accept()
        print('we are accept a connection from ',sockname)
        print('Socket name',sc.getsockname())
        print('Socket peer',sc.getpeername())
        message = recvall(sc,16)
        print('Incoming sixteen-octet message:',repr(message))
        sc.sendall(b'Farewell,client')
        sc.close()
        print('reply sent ,socket closed')


def client(host,port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect((host,port))
    print('client has been assigned socket name',sock.getsockname())
    sock.sendall(b'Hi there server')
    reply = recvall(sock,16)
    print('the server said ',repr(reply))
    sock.close()


if __name__ == '__main__':
    choices = {'client':client,'server':server}
    parser = argparse.ArgumentParser(description='send and recieve over tcp')
    parser.add_argument('role',choices=choices,help='which role to play')
    parser.add_argument('host',help='interface the server listen at:host the client sends to')
    parser.add_argument('-p',metavar='PORT',type=int,default=1060,help='tcp port (default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host,args.p)