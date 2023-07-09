
# coding: utf-8

# In[ ]:


""" 修改数据后，保存至excel文件，并更新相关数据 

@param 修改excel后，需要更新
sheets_ordereddict as OrderedDict, 工作表名称及数据df有序字典
sheets_dict as dict, 工作表名称及数据df字典
sheet_name as str, 工作表名称
sheet_data as df, 工作表内数据
sheet_list as list, 工作表名称列表
"""


# In[ ]:


from pandas import Series, DataFrame
from IPython.display import display
from  openpyxl import load_workbook

import pandas as pd
import numpy as np
import xlwings as xw
import xlrd
import openpyxl
import xlwt


# In[ ]:


def update_data(df, file_path, sheetName):
    

    with pd.ExcelWriter(file_path, engine='openpyxl', mode='a', if_sheet_exists='new') as writer:
        df.to_excel(writer, sheet_name = sheetName)
            
        sheets_ordereddict = pd.read_excel(file_path, sheet_name = None)    # 返回OrderedDict（有序字典）
        sheets_dict = dict()
        for sheet_name, sheet_data in sheets_ordereddict.items():
            sheets_dict[sheet_name] = sheet_data

        sheet_list = list(sheets_dict.keys())    # 储存工作表名称，为list
        


