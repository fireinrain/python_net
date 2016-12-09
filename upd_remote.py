#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# 运行在不同机器上的upd服务器和客户端

import argparse, socket,sys,random
from datetime import datetime

MAX_BYTES = 65535


# 服务端
def server(interface,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('服务器监听在：{}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(MAX_BYTES)
        if random.random() < 0.5:

            print('打算放弃来自：{}的数据包'.format(address))
            continue
        text = data.decode('utf-8')
        print('客户端{}-发送了-{}'.format(address,text))
        message = '数据长度为{}bytes'.format(len(data))
        sock.sendto(message.encode('utf-8'),address)




# 客户端
def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # text = '时间是：{}'.format(datetime.now())
    while True:
        text = input('请发送对话：')
        data = text.encode('utf-8')

        sock.sendto(data, ('127.0.0.1', port))
        print('操作系统在{}认证'.format(sock.getsockname()))
        data, address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')
        print('服务器{}返回的数据：{}'.format(address, text))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='在本地发送udp数据包')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('-p', metavar='PORT', type=int, default=1060, help='udp port(default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)