# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""
import os

import time,pytest


if __name__ == '__main__':
    time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    # pytest.main(['-v','.\\ConftestFile\\test_rtc.py','--html','.\\report\\report-%s.html--self-contained-html'%time])
    pytest.main(['-v','.\\ConftestFile\\test_rtc.py','--html','.\\report\\report-%s.html'%time])
