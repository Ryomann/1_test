# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""

# -*- coding: utf-8 -*-
import os
import time
import logging
import sys
from functools import wraps
import traceback




# log_dir1 = os.path.join(os.path.dirname(os.path.dirname(__file__)), "logs")
log_dir1 = os.path.abspath("..\\log")
today = time.strftime('%Y%m%d', time.localtime(time.time()))
full_path = os.path.join(log_dir1, today)
if not os.path.exists(full_path):
    os.makedirs(full_path)
# log_path = os.path.join(full_path, "aaa.log")
log_path = os.path.abspath(".\\log\\%s.log"%(today))
print(log_path)

def get_logger():
    # 获取logger实例，如果参数为空则返回root logger
    logger = logging.getLogger("inter")
    if not logger.handlers:
        # 指定logger输出格式
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')

        # 文件日志
        file_handler = logging.FileHandler(log_path, encoding="utf8")
        file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式

        # 控制台日志
        console_handler = logging.StreamHandler(sys.stdout)
        console_handler.formatter = formatter  # 也可以直接给formatter赋值

        # 为logger添加的日志处理器
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

        # 指定日志的最低输出级别，默认为WARN级别
        logger.setLevel(logging.INFO)
    #  添加下面一句，在记录日志之后移除句柄
    return logger

#LOG = get_logger(file_log=file_stream, level='INFO')
# 然后定义一个装饰器文件
#
# 在这里引用wraps, 一个装饰器的装饰器，目的为了保持引用进来的函数名字不发生变化

def logger(func):
    @wraps(func)
    def log(*args, **kwargs):
        try:
            print("当前运行方法", func.__name__)
            return func(*args, **kwargs)
        except Exception as e:
            get_logger().error(f"{func.__name__} is error,here are details:{traceback.format_exc()}")

    return log




def start():
    print("666")
