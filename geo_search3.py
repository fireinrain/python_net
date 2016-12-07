#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

import http.client
import json
from urllib.parse import quote_plus
import time

base = 'maps/api/geocode/json'

def geocode(address):
    path = '{0}?address={1}&sensor=false'.format(base,quote_plus(address))
    connection = http.client.HTTPConnection('maps.google.com',timeout=5)
    connection.request('GET',path)
    time.sleep(1)
    raw_replay = connection.getresponse().read()
    print(raw_replay)
    replay = json.load(raw_replay.decode('utf-8'))
    print(replay['results'][0]['geometry']['location'])


if __name__ == '__main__':
    geocode('207 N.Defiance St,Archbold,OH')
