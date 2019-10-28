# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""
import xlrd,xlwt,os
import xlwt

def datacel(filrpath,sheetnum,nrows):
    try:
        file = xlrd.open_workbook(filrpath)
        me = file.sheets()[sheetnum]

        id = me.cell(nrows,0).value
        name =  me.cell(nrows,1).value
        key = me.cell(nrows,2).value
        content = me.cell(nrows,3).value
        url = me.cell(nrows,4).value
        mode =me.cell(nrows,5).value
        expection = me.cell(nrows,6).value
        result = me.cell(nrows,7).value

        return id,name,key,content,url,mode,expection,result
    except Exception as e:
        print('打开测试用例失败，原因是:%s' % e)
        return
if __name__ == '__main__':

    # datacel(os.path.abspath('..\\test_case_data\\case.xlsx'))
    path = os.path.abspath('..\\test_data\\case.xlsx')
    print(datacel(path,0,1))