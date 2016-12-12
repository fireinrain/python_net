#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# 使用udp广播
import argparse,socket

BUFFSIZE = 65535



# 服务端
def server(interface,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((interface, port))
    print('服务器监听在：{}'.format(sock.getsockname()))
    while True:
        data, address = sock.recvfrom(BUFFSIZE)
        text = data.decode('utf-8')
        print('客户端{}-发送了-{}'.format(address,text))





# 客户端
def client(network,port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)
    text = 'broadcast datagram'
    sock.sendto(text.encode('utf-8'),(network,port))


if __name__ == '__main__':
    choices = {'client': client, 'server': server}
    parser = argparse.ArgumentParser(description='在本地发送udp数据包')
    parser.add_argument('role', choices=choices, help='which role to play')
    parser.add_argument('help',help='interface the server listen at')
    parser.add_argument('-p', metavar=' PORT', type=int, default=1060, help='udp port(default 1060)')
    args = parser.parse_args()
    function = choices[args.role]
    function(args.host,args.p)
