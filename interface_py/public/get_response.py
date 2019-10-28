# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""
import os,json

from public.get_excel import datacel
from public.encrypt import encrypt
from public.t_requests import requ

# 获取响应值
def resp(excelpath,sheetnum,nrows,domain,key,isencrypt):

    # key1= "rtc18062315294512068"

    id, name, key1, content, url, mode, expection, result = datacel(excelpath,sheetnum,nrows)

    url = domain + url
    # print("url",url)
    if mode== 'POST' and isencrypt is True:
        encrypy_paramer = encrypt(key,content)
        response =requ().post(url,encrypy_paramer)
        return response
    elif mode == 'GET':
        response = requ().get(url,content)
        return response
    else:
        print("sorry,POST or GET!")


if __name__ == '__main__':
    excelpath = os.path.abspath("../test_data/case.xlsx")
    domain = "http://47.97.43.108"

    key = "rtc18062315294512068"
    re =resp(excelpath,0,5,domain,key,isencrypt=True)
    print(re)
    # path = os.path.abspath("..\\test_data\\case.xlsx")
    # a = datacel(path, 0, 5)
    #
    # parm = a[3]
    # # print(a)
    #
    # key = "rtc18062315294512068"
    #
    # e = encrypt(key, parm)
    # # aaa = e['accountId']
    # # print(e)
    # domain = "http://47.97.43.108"
    # url_aa = domain + "/rtccloud/im/disuse"
    # # url_aa = domain + "/rtccloud/im/login"
    #
    # res = requests.post(url=url_aa, data=json.dumps(e), headers={'Content-Type': 'application/json'}).text
    # print("响应 :" + res)
