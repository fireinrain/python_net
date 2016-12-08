#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
# 将主机名转换为ip

import socket

if __name__ == '__main__':
    host_name = 'www.lzycoder.cc'
    addr = socket.gethostbyname(host_name)
    print('the ip address is {},the hostname is {}.'.format(addr,host_name))

