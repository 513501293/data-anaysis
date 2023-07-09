# Date: 2023/06/27
''' 打开并读取excel文件 '''

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

''' 输入文件位置，打开excel，并返回打开时间和所有的工作表名称及数据
@param
path as str：文件位置
filename as str：文件名
start_time, end_time, t as float：开始时间，结束时间，用时

@return
sheets_dict as dict: excel文件中所有的工作表，sheets = {'工作表名称': df}
df as dataframe：Excel中的数据
'''





def excel_to_df(path) -> DataFrame:
    df = pd.read_excel(path, 'test1')

    return df

# test Collection
# excel_path = r'C:\Users\yiru.wang\PycharmProjects\pythonProject1\test.xlsx'
# data = excel_to_df(excel_path)
#
# print(data)
