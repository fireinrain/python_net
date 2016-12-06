#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N.Defiance St,Archbold,OH'
    print(Geocoder.geocode(address)[0].coordinates)