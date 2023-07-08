# Date: 2023/07/02
""" 对df标签进行标准化处理
1. 题目标准化
2. 题型标准化

@return
(dimension, type_of_question) as tuple: (维度，题型）
dimension_type_list as list: 储存所有标准化(维度，题型）的列表
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

# 自定义类
from Question import Question

# 常用标准化维度、题型列表（From 问卷星）
global common_dimensions_list
global question_type_list

common_dimensions_list = ['用户ID', '姓名', '性别', '年龄', '学历', '婚姻', '国家', '地区', '省市', '手机', '职业',
                          '行业', '学历', '家庭人口']
common_question_type_list = ['单选', '多选', '填空', '排序', '量表']

# test df
df = DataFrame({'1. 您的姓名（填空）：': ['A', 'B', 'C'],
                'B2_您的年龄【单选】：': ['2-3', '5-6', '7-8'],
                'C3_4您的婚姻状态[单选]': ['已婚', '未婚', '保密'],
                'D3_4_您的家庭常住人口数量：': ['1', '2', '3'],
                '您目前拥有的车辆（多选）：': [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]})

# 提取df中的题目和题型
question_list = df.columns.to_list()

# 将问卷问题转化为标准化维度
""" 将问卷问题转化为标准化维度
1. 若问题中包含常用维度中的字符，则转化为常用维度，需要人工查验
2. 返回未被处理的问题列表，人工标准化
3. 再次人工查验
4. 返回问题类列表？？？？？

@param
question_list as list：储存问卷问题的列表
"""
unpaired_question_list = []


def standardize_question(question):
    for dimension in common_dimensions_list:

        if dimension in question:
            unpaired_question_list.remove(question)
            print('请检查下列问题与标准化维度是否匹配（Y/N）：')
            print('问题：' + question)
            print('维度：' + dimension)
            result = input().upper()

            if result == 'Y':
                question = dimension

            elif result == 'N':
                print('请输入维度名称：')
                question = input()



    return question


# 去除序号及符号
""" 去除问卷问题中的序号及标点符号（可选）
1. 去除序号
2. 去除末尾标点
3. 切分问题与题型，保存为列表

@param
q_t as list: [问卷问题，题型]列表

@return
cleaned_q_t_list as list：去除序号和符号后的问卷问题列表"""


def clean_question_list(question_list):
    # 创建清理后的列表
    cleaned_q_t_list = []

    # 去除序号、符号
    for question in question_list:

        question = re.search('[\u4e00-\u9fa5].*[^:?：？]', question).group()  # 匹配汉字，去除结尾的冒号及问号
        q_t = re.findall('[^(\[（【]+[\u4e00-\u9fa5]+', question)  # 切分题目和题型
        unpaired_question_list.append(q_t[0])


        q_t[0] = standardize_question(q_t[0])


        # 处理不包含题型的问题
        if len(q_t) <= 1:
            q_t.append('None')  # 增加空值

        cleaned_q_t_list.append(q_t)


    return cleaned_q_t_list


# 生成去除序号、符号后的问题列表
cleaned_q_t_list = clean_question_list(question_list)

# df.columns = cleaned_q_t_list

#
#
# def standardize_question(question_list):
#     standardized_question_list = []
#     for question in question_list:
#         question_type_list = re.findall('[^(\[（【]+[\u4e00-\u9fa5]+', question)
#

#
#         question_type = Question(question_type_list[0], question_type_list[1])
#         question_type.show()
#         standardized_question_list.append(question_type)
#
#     return standardized_question_list
#
#
# standardized_question_list = standardize_question(cleaned_question_list)

print(question_list)
print(cleaned_q_t_list)
print(unpaired_question_list)

# df.columns = cleaned_question_list
# print(df)
