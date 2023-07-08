# Date: 2023/07/04
""" 打开excel文件，并将工作表数据储存为df
1. pandas打开excel
2. 提取指定工作表数据，返回df
"""

# 数据分析包
import pandas as pd
from pandas import DataFrame
import numpy as np
import openpyxl


def excel_to_df(path) -> DataFrame:
    df = pd.read_excel(path, 'test1')

    return df


# test Collection
# excel_path = r'C:\Users\yiru.wang\PycharmProjects\pythonProject1\test.xlsx'
# data = excel_to_df(excel_path)
#
# print(data)
