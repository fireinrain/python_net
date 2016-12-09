#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 将主机名转换为ip

import socket

if __name__ == '__main__':
    host_name = 'www.liuzhaoyang.com'
    addr = socket.gethostbyname(host_name)
    print('the ip address is {},the hostname is {}.'.format(addr,host_name))
    # for i in range(49151):
    #     try:
    #         my_port = socket.getservbyport(i)
    #         print("the server--{}-- at-- port-- {}".format(my_port,i))
    #     except Exception as e:
    #         continue

    print(socket.socket().fileno())
    with open('bytes.txt','rb') as f:
        print(f.fileno())
