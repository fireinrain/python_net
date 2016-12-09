#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 使用自环接口的upd服务器和客户端
# 稍作修改可以实现双向发送信息

import argparse,socket
from datetime import datetime

MAX_BYTES = 65535

# 服务端
def server(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    sock.bind(('127.0.0.1',port))
    print('服务器监听在：{}'.format(sock.getsockname()))
    while True:
        data,address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')
        print('客户端在{}发送了{}'.format(address,text))
        # text = '你的数据时{}字节长'.format(len(data))
        # data = text.encode('utf-8')

        text = input('发送给客户端：')
        data = text.encode('utf-8')
        sock.sendto(data,address)
        
# 客户端
def client(port):
    sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # text = '时间是：{}'.format(datetime.now())
    while True:
        text = input('请发送对话：')
        data = text.encode('utf-8')

        sock.sendto(data,('127.0.0.1',port))
        print('操作系统在{}认证'.format(sock.getsockname()))
        data,address = sock.recvfrom(MAX_BYTES)
        text = data.decode('utf-8')
        print('服务器{}返回的数据：{}'.format(address,text))

if __name__ == '__main__':
    choices = {'client':client,'server':server}
    parser = argparse.ArgumentParser(description='在本地发送udp数据包')
    parser.add_argument('role',choices=choices,help='which role to play')
    parser.add_argument('-p',metavar='PORT',type=int,default=1060,help='udp port(default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.p)