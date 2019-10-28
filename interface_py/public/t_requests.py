# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""
import requests, json
import time
from public.encrypt import encrypt
from public.get_excel import *
class requ():
    def __init__(self):
        self.headers = {'Content-Type': 'application/json'}
        self.t = int(round(time.time() * 1000))

    def get(self, url, params):  # get消息
        try:
            r = requests.get(url, params=params, headers=self.headers)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            # return {'code': 0, 'result': json_response}
            return json_response
        except Exception as e:
            return e

    def post(self, url, params):  # post消息
        try:
            r = requests.post(url=url, data=json.dumps(params), headers=self.headers).text

            return r
        except Exception as e:
            return e

    def delfile(self, url_a, params):  # 删除的请求
        try:
            del_word = requests.delete(url=url_a, params=params, headers=self.headers).text
            json_response = json.loads(del_word.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            return {'code': 1, 'result': 'del请求出错，出错原因:%s' % e}

    def putfile(self, url, params):  # put请求
        try:
            data = json.dumps(params)
            me = requests.put(url, data)
            json_response = json.loads(me.text)
            return {'code': 0, 'result': json_response}
        except Exception as e:
            return {'code': 1, 'result': 'put请求出错，出错原因:%s' % e}



















if __name__ == '__main__':
    re = requ()
    # path = os.path.abspath("..\\test_data\\case.xlsx")
    # listid, listname, listkey, listconeent, listurl, listfangshi, listqiwang = datacel(path)
    #
    # parm = listconeent[1]
    #
    # key = "rtc18062315294512068"
    # path = os.path.abspath("..\\test_data\\case.xlsx")
    #
    # e = encrypt(key, parm)
    #
    # domain = "http://47.97.43.108"
    # url_aa = domain + "/rtccloud/im/create"
    # print('=====',e)
    # # print(url_aa)
    # # print(e,type(e))
    # res = requests.post(url=url_aa, data=json.dumps(e), headers={'Content-Type': 'application/json'}).text
    # res1 = re.post(url_aa,e)
    # print('ceshi',res1)
    # # print(json.dumps(e))
    # print('33333333333',res,type(res))
    # # print("响应 :" + res1)
