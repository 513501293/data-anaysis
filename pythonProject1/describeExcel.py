# Date: 2023/07/09
""" 描述Excel文件情况
1. 返回包含的工作表名称
2. 返回指定工作表包含的数据情况
"""
# 数据分析包
import pandas as pd
from pandas import DataFrame
import numpy as np
import xlwings
import openpyxl

# 时间包
import time

# 文字处理包
import re

# test
divider = '=====================================\n'

# 输入文件位置
# path = input('请输入文件位置：')
path = r'/Users/yiruwong/Desktop/testfile.xlsx'  # test


def open_excel(path):
    # 提取文件名
    filename = path.split('/')[-1]

    try:
        print('正在打开文件：%s' % path)

        # 开始计时
        start_time = time.perf_counter()
        # 打开文件，返回所有工作表名称
        sheets_dict = pd.read_excel(path, sheet_name=None)

        # 结束计时，计算用时
        end_time = time.perf_counter()
        t = round(end_time - start_time, 2)

        print('%s已打开，用时%s秒\n' % (filename, t))
    except:
        # 若文件打开失败，则报错
        print('%s打开失败\n' % filename)
        quit()

    return sheets_dict


sheets_dict = open_excel(path)

print(sheets_dict)
