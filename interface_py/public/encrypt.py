# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""


import time
from public.get_excel import datacel
import os, json, hashlib
import requests



def encrypt(key, pararmeter):
    try:
        # 时间戳

        t = int(round(time.time() * 1000))
        pararmeter_dict = json.loads(pararmeter)
        # print(pararmeter_dict)
        pararmeter_dict['timeStamp'] = str(t)
        # print("参数 + 时间戳：",pararmeter_dict)
        pararmeter_assii = sorted( pararmeter_dict.items())
        pararmeter_assii = dict(pararmeter_assii)
        # print("assii",pararmeter_assii,type(pararmeter_assii))
        # sign
        parm = []
        for i in pararmeter_assii.items():
            if type(i[1]) is int:
                mm = ("%s=%d&" % (i[0], i[1]))
                parm.append(mm)
                print(type(parm))
            else:
                mm = str(i[0]) + "=" + str(i[1]) + '&'
                parm.append(mm)
        # print("parm:",parm)
        # list_parm.append(key)
        # 转换为str
        parm = [str(i) for i in parm]
        str_parm = ''.join(parm) + key
        # print(str_parm)
        # 转md5
        md5_object = hashlib.md5()
        md5_object.update(str_parm.encode(encoding='UTF-8'))
        md5_result = md5_object.hexdigest()
        # print(md5_result)
        b = {"sign": md5_result, "timeStamp": str(t)}
        pararmeter_finally = json.loads(pararmeter)
        pararmeter_finally.update(b)
        print("finally 参数:",pararmeter_finally)
        return pararmeter_finally
    except Exception as e:
        print("加密出错：",e)


if __name__ == '__main__':
    path = os.path.abspath("..\\test_data\\case.xlsx")
    a = datacel(path,0,5)
    parm = a[3]
    print(a)
    key = "rtc18062315294512068"
    e = encrypt(key, parm)
    domain = "http://47.97.43.108"
    url_aa = domain + "/rtccloud/im/answer"
    res = requests.post(url=url_aa, data=json.dumps(e), headers={'Content-Type': 'application/json'}).text
    print("响应 :" + res)
