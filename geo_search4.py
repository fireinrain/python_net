#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com
import socket
from urllib.parse import quote_plus

request_text = """GET /maps/api/geocode/json?address={}&sensor=false HTTP/1.1\r\n\
                  Host:maps.google.com:80\r\n\
                  User-Agent:geo_search4.py(Foundation of Python Network Programming)\r\n
                  Connection:close\r\n
                  \r\n
                """

def geocode(address):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sock.connect(('maps.google.com',80))
    request = request_text.format(quote_plus(address))
    sock.sendall(request.encode('ascii'))
    raw_reply = b''
    while True:
        data_get = sock.recv(4096)
        if not data_get:
            break
        else:
            raw_reply += data_get
    print(raw_reply.decode('utf-8'))

if __name__ == '__main__':
    geocode('207 N.Defiance St,Archbold,OH')
