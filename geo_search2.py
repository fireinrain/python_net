#! /usr/bin/python3
# _encoding:utf-8_
# Written by liuzhaoyang
# wcontact:liu575563079@gmail.com

# 使用requests模块来访问谷歌地图的api，并接受返回的json数据
# 解析出来
import requests

def geocode(address):
    parameters = {'address':address,'sensor':'false'}
    base = 'http://maps.googleapis.com/maps/api/geocode/json'
    response = requests.get(base,params=parameters)
    # print(response.text) 获得的是json字符串
    answer = response.json()    #将json字符串转化为字典格式
    print(answer)
    print(answer['results'][0]['geometry']['location'])

if __name__ == '__main__':
    geocode('207 N.Defiance St,Archbold,OH')