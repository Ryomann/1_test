# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""
import json
import os

from public.get_response import resp
from public.get_excel import datacel

def actul_result(excelpath,sheetnum,nrows,domain,key,isencrypt):

        result = resp(excelpath,sheetnum,nrows,domain,key,isencrypt)
        print("result:",result)

        try:
            dict_r = dict(json.loads(result))
            # result1 = list(dict_r.items())
            actul_data = "data = " + str(dict_r.get("data"))

            actul_result1 = "code=" + str(dict_r.get('code'))
            actul_result2 = "message=" + str(dict_r.get("message"))
            actul_result = []
            actul_result = [actul_result1,actul_result2]

            return actul_result,actul_data
        except Exception as e:
            print("响应为：",result,e)
def expect_result(filepath,sheetnum,nrows):
    result1 = datacel(filepath,sheetnum,nrows)[6]
    expect_result = result1.split(",")
    return expect_result



if __name__ == '__main__':
    excelpath = os.path.abspath("D:\\miw_work\\project\\interface_py/test_data/case.xlsx")
    domain = "http://47.97.43.108"
    num = 0

    key = "rtc18062315294512068"
    r = actul_result(excelpath,0,5,domain,key,isencrypt=True)
    print(r)