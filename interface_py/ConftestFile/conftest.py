# -*- coding: utf-8 -*-
""" 
@author: 
@file:
@time: 
"""




def pytest_configure(config):
    config._metadata['测试地址'] = '192.168.50.XXX'


import pytest
from py._xmlgen import html

@pytest.mark.optionalhook
def pytest_html_results_summary(prefix, summary, postfix):
    prefix.extend([html.p("测试人: ")])


#============
# from datetime import datetime
# import pytest
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_header(cells):
#     cells.insert(2, html.th('Description'))
#     cells.insert(3, html.th('Time', class_='sortable time', col='time'))
#     # cells.insert(1,html.th("Test_nodeid"))
#     cells.pop()
#
# @pytest.mark.optionalhook
# def pytest_html_results_table_row(report, cells):
#     cells.insert(2, html.td(report.description))
#     cells.insert(3, html.td(datetime.utcnow(), class_='col-time'))
#     # cells.insert(1,html.td(report.nodeid))
#     cells.pop()
#
# @pytest.mark.hookwrapper
# def pytest_runtest_makereport(item, call):
#     outcome = yield
#     report = outcome.get_result()
#     report.description = str(item.function.__doc__)
#     report.nodeid = report.nodeid.encode("utf-8").decode("unicode_escape")   #设置编码显示中文
#
#
