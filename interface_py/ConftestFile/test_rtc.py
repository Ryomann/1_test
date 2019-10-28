# -*- coding: utf-8 -*-
"""
@author:
@file:
@time:
"""
# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""
import os
import time
import pytest
from public.determine import expect_result, actul_result


@pytest.fixture(scope="session")
def key():
    key = "rtc18062315294512068"
    return key
@pytest.fixture(scope="session")
def excelpath():
    # excelpath = os.path.abspath("D:\\miw_work\\project\\interface_py/test_data/case.xlsx")
    excelpath = os.path.abspath("D:\\miw_work\\project\\interface_py/test_data/case.xlsx")
    return excelpath
@pytest.fixture(scope="class")
def domain():
    domain = "http://47.97.43.108"
    return domain
class Test_account:
    @pytest.mark.parametrize("num",[1,2])
    def test_accout_create(self,excelpath,domain,key,num):
        a = actul_result(excelpath,0,num,domain,key,isencrypt=True)[0]
        e = expect_result(excelpath,0,num)
        print(a,e)
        assert a == e
    #
    # def test_accout_002(self,excelpath,domain,key):
    #     a = actul_result(excelpath,0,2,domain,key,isencrypt=True)[0]
    #     e = expect_result(excelpath,0,2)
    #     assert a == e

    def test_accout_003(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 3, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 3)
        print(a,e)
        assert a == e
    def test_accout_004(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 4, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 4)
        print(a,e)
        assert a == e
    def test_accout_005(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 5, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 5)
        print(a,e)
        assert a == e
    def test_accout_006(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 6, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 6)
        print(a,e)
        assert a == e
class Test_device:
    def test_device_007(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 7, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 7)
        print(a,e)
        assert a == e
    def test_device_008(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 8, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 8)
        print(a,e)
        assert a == e
    def test_device_009(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 9, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 9)
        print(a,e)
        assert a == e
    def test_device_010(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 10, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 10)
        print(a,e)
        assert a == e
    def test_device_011(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 11, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 11)
        print(a,e)
        assert a == e
    def test_device_012(self,excelpath,domain,key):
        a = actul_result(excelpath, 0, 12, domain,key,isencrypt=True)[0]
        e = expect_result(excelpath, 0, 12)
        print(a,e)
        assert a == e
if __name__ == '__main__':
    os.system("d:"
              "cd D:\\miw_work\\project\\interface_py\\ConftestFile"
              "pytest --html=reportname3.html")
    #