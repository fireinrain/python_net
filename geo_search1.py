#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com


# 使用pygeocoder模块来查询目标位置的经纬度
from pygeocoder import Geocoder

if __name__ == '__main__':
    address = '207 N.Defiance St,Archbold,OH'
    print(Geocoder.geocode(address)[0].coordinates)