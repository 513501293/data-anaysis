# Date: 2023/07/04
""" 储存各种数据清洗方法
1. 检查数据一致性
2. 检查并处理空值
3. 检查重复值
4. 检查异常值
5. 检查无意义值
"""

# 数据分析包
import pandas as pd
from pandas import DataFrame
import numpy as np
import openpyxl

# 时间包
from dateutil.parser import parse
from datetime import datetime

# 自定义方法包
from openExcel import excel_to_df
from input_to_boolean import input_to_boolean

# test Collection
excel_path = r'C:\Users\yiru.wang\PycharmProjects\pythonProject1\test.xlsx'
ori_data = excel_to_df(excel_path)
# ori_data.columns = list(map(str, (ori_data.columns.values.tolist())))

# print(data)

# 检查并清理空值
""" 处理空值 
清理必答题中含有空值的用户数据(行),非必答题含有空值则保留
1. 根据题目性质, 将原始数据df分为必答题df和非必答题df
2. 对必答题df进行处理, 若含有空值, 则返回该行索引; 或手动输入要删除的行的索引
3. 从原始数据df中删除对应行,
4. 返回清理空值后的数据集df

@param 
df as df: 传入的数据集
unsorted_ques_df，required_ques_df，optional_ques_df as df：必答题、非必答题、未处理数据集
required_ques_list，optional_ques_list as list：必答题、非必答题列表
result as Boolean：用户输入结果
na_rows, na_cols as Series: 含有空值的行和列
na_rows_index as list: 含有空值的行的索引列表
report as df：数据概况

@return
cleaned_NaN_df as df: 清除必答题含有空值的行后的数据集
"""
# 必答题、非必答题列表
required_ques_list = ['序号', '姓名', '性别', '年龄']
optional_ques_list = ['上一辆车的车型', '上一辆车购买时间']


def clean_NaN(df: DataFrame) -> DataFrame:
    print("开始清理数据空值...\n\n"
          "正在依据必答/非必答题进行数据清理...\n"
          "正在检索原始数据...\n")

    # 提取必答题、非必答题、未处理、处理后数据
    unsorted_ques_df = df.copy()
    required_ques_df = DataFrame()
    optional_ques_df = DataFrame()
    cleaned_NaN_df = DataFrame()

    # 历遍原始数据，将数据分为必答题，非必答题两类，同时返回未处理问题df，人工分类
    for question in unsorted_ques_df.columns.values:
        # 检索必答题
        if question in required_ques_list:
            required_ques_df[question] = unsorted_ques_df.pop(question)
        # 检索非必答题
        elif question in optional_ques_list:
            optional_ques_df[question] = unsorted_ques_df.pop(question)
        # 标注未明确是否必答的题目
        else:
            print(f'下列问题需人工标注是否为必答题（Y/N）\n “{question}”')
            result = input_to_boolean()
            if result is True:
                required_ques_df[question] = unsorted_ques_df.pop(question)
                required_ques_list.append(question)
            elif result is False:
                optional_ques_df[question] = unsorted_ques_df.pop(question)
                optional_ques_list.append(question)

    # 返回分类处理结果
    print(f'原始数据包含题目数量为{df.shape[1]}')
    print(f'必答题数量为{required_ques_df.shape[1]}, 包含如下维度：{required_ques_df.columns.values.tolist()}')
    print(f'非必答题数量为{optional_ques_df.shape[1]}, 包含如下维度：{optional_ques_df.columns.values.tolist()}')
    print('\n所有题目已标注必答/非必答\n' if df.shape[1] == required_ques_df.shape[1] + optional_ques_df.shape[
        1] else '尚有题目未被处理\n')

    # 筛选必答题数据，提取无空值的行号，有空值的行号，被分别返回该行的原始数据，人工查验
    print('是否进行下一步数据清理（Y/N）？')
    result = input_to_boolean()
    if result is True:

        # # 返回不含空值的行
        # # all：df中的所有列
        # not_na_rows = required_ques_df[required_ques_df.notna().T.all()]
        # print(f'非空数据集为：\n{not_na_rows}\n')

        # 返回含有空值的行与列
        # any: df中的任意列
        na_rows = required_ques_df[
            required_ques_df.isna().T.any()]  # 转置:df.isnull().T.any(),得到的每一行求any()计算的结果,输出为行的Series
        na_cols = required_ques_df.isnull().any()  # 非转置:df.isnull().any(),得到的每一列求any()计算的结果,输出为列的Series

        # 若存在含有空值的行
        if len(na_rows) > 0:
            print(f'下列必答列存在空值：\n{na_cols}\n')
            print(f'下列行存在空值：\n{na_rows}\n')

            # 删除含有空值的数据行
            na_rows_index = na_rows.index.tolist()
            print(f'是否从原始数据中删除上述行，即第{na_rows_index}行（Y/N）？')
            result = input_to_boolean()

            # 删除必答题中含有空值的全部行
            if result is True:
                cleaned_NaN_df = df.drop(index=na_rows_index)

            # 删除必答题中含有空值的部分行
            elif result is False:
                print('是否要手动删除指定行（Y/N）？')
                result = input_to_boolean()

                # 手动输入行号并删除
                if result is True:
                    print('请输入需要删除的数据的【行号】（不是序号），若存在多个，以空格分隔')
                    na_rows_index = list(input().split())
                    # 将字符串转换为数字
                    for i in range(len(na_rows_index)):
                        try:
                            na_rows_index[i] = int(na_rows_index[i])
                        except:
                            print('非法输入！')
                            quit()  # ======================================
                    # 删除指定行
                    cleaned_NaN_df = df.drop(index=na_rows_index)

                elif result is False:
                    quit()  # =======================================

        # 若不存在空值
        elif len(na_rows) == 0:
            print('必答题不存在空值')
            cleaned_NaN_df = df.copy()

    elif result is False:
        quit()  # ========================

    print('\n空值清洗完成！\n')

    report = DataFrame({'是否包含空值': cleaned_NaN_df.isnull().any().values,
                        '计数': cleaned_NaN_df.count().values},
                       index=cleaned_NaN_df.columns.values)


    print(f'数据集描述：\n{report}\n')
    print(f'请人工检查清洗后数据集：\n{cleaned_NaN_df}\n')

    return cleaned_NaN_df



# 检查并清理重复值
""" 处理重复值
清理重复的数据
1. 删除数据完全相同的行
2. 删除特定列数据完全相同的行

@param
df as df：原始数据集
uncleaned_df as df： 未处理的数据集（不含序号）
duplicated_rows as df: 数据完全相同的行，返回除第一条行的所有行
duplicated_rows_index as list: 重复行的行号
result as boolean：用户输入结果
df_columns_list as list: 数据集包含的列名（不含序号）
check_duplication_list as list: 待检查的列的列名列表
aimed_cols_df as df：待检查的列的数据集
wrong_cols_list as list：返回错误输入内容
report as df：数据概况


@return
cleaned_duplication_df as df: 清洗重复值后的数据集
"""


# 需要检查重复值的问题列表
# check_duplication_list = ['姓名', 'IP']


def clean_duplication(df: DataFrame) -> DataFrame:
    print("开始清理数据重复值...\n\n"
          "正在检索原始数据...\n")

    # 未处理数据集、清理重复值后的数据集
    uncleaned_df = df.copy().drop('序号', axis=1)  # 序号可以允许重复，数据清洗完成后重新赋值
    cleaned_duplication_df = df.copy()

    print('正在检索重复行...\n')

    # 返回重复行（即行内数据完全一致）
    duplicated_rows = uncleaned_df[uncleaned_df.duplicated()]

    # 若存在重复行
    if len(duplicated_rows) > 0:
        print(f'存在下列重复行（即行内数据完全一致）：\n{duplicated_rows}\n')

        # 返回重复行行号
        duplicated_rows_index = duplicated_rows.index.tolist()
        print(f'是否从原始数据中删除上述行，即第{duplicated_rows_index}行（Y/N）？\n')
        result = input_to_boolean()

        # 删除重复行
        if result is True:
            cleaned_duplication_df = df.drop(index=duplicated_rows_index)

        elif result is False:
            quit()  # ===============================

    # 若不存在重复行
    elif len(duplicated_rows) == 0:
        print('不存在重复行（即行内数据完全一致）\n')

    # 检查指定列是否存在重复值
    print('是否需要检查指定列存在重复值（Y/N）？')

    result = input_to_boolean()
    if result is True:
        # 返回数据集包含的列名（不含“序号”）
        df_columns_list = uncleaned_df.columns.values.tolist()
        print(f'数据集包含以下列：\n{df_columns_list}\n')
        print(
            '请输入待检查的【列名】（如“姓名”、“IP”等），若存在多个，以空格分隔（返回在所有输入列上完全一致的行，如同“姓名”并且同“IP”）')
        check_duplication_list = list(input().split())

        # 检查用户输入的列名是否存在于数据集中
        if all(col in df_columns_list for col in check_duplication_list) and len(check_duplication_list) > 0:
            # 提取待检查的列数据
            aimed_cols_df = cleaned_duplication_df[check_duplication_list]
            print('正在检索重复行...\n')

            # 返回重复行（即行内数据完全一致）
            duplicated_rows = aimed_cols_df[aimed_cols_df.duplicated()]

            # 处理重复值
            # 若存在重复行
            if len(duplicated_rows) > 0:
                print(f'存在下列重复行（即行内数据完全一致）：\n{duplicated_rows}')

                # 返回重复行行号
                duplicated_rows_index = duplicated_rows.index.tolist()
                print(f'是否从原始数据中删除上述行，即第{duplicated_rows_index}行（Y/N）？')
                result = input_to_boolean()

                # 删除重复行
                if result is True:
                    cleaned_duplication_df = cleaned_duplication_df.drop(index=duplicated_rows_index)

                elif result is False:
                    print('是否需要手动删除指定行（Y/N）？')
                    result = input_to_boolean()
                    if result is True:
                        print('请输入需要删除的数据的【行号】（不是序号），若存在多个，以空格分隔')
                        duplicated_rows_index = list(input().split())
                        # 将字符串转换为数字
                        for i in range(len(duplicated_rows_index)):
                            try:
                                duplicated_rows_index[i] = int(duplicated_rows_index[i])
                            except:
                                print('非法输入！')
                                quit()  # ======================================
                        # 删除指定行
                        cleaned_duplication_df = df.drop(index=duplicated_rows_index)

                    elif result is False:
                        quit()  # =======================================

            # 若不存在重复行
            elif len(duplicated_rows) == 0:
                print('不存在重复行（即行内数据完全一致）')

        # 若存在错误输入
        else:
            if len(check_duplication_list) == 0:
                print('输入为空！请重新输入')
                quit()
            else:
                wrong_cols_list = []
                for col in check_duplication_list:
                    if col not in df_columns_list:
                        wrong_cols_list.append(col)
                        print(f'数据集中不存在{wrong_cols_list}列，请重新输入')
                        quit()  # =============================================

    print('重复值清洗完成！\n')

    report = DataFrame({'是否包含重复值': cleaned_duplication_df.isnull().any().values,
                        '计数': cleaned_duplication_df.count().values},
                       index=cleaned_duplication_df.columns.values)
    report.index.name = '维度'

    print(f'数据集描述：\n{report}\n')
    print(f'请人工检查清洗后数据集：\n{cleaned_duplication_df}\n')

    return cleaned_duplication_df



# 检查并清洗异常值
""" 处理异常值
1. 作答时间：
    1.1 描述作答时间列
"""
# 需要进行异常值检查及处理的维度列表
outlier_check_list = ['作答时间']


def clean_outlier(df):
    print("开始清理数据异常值...\n\n"
          "正在检索原始数据...\n")

    df_columns_list = df.columns.values.tolist()
    cleaned_outlier_df = df.copy()

    # 判断数据集中是否存在需要进行异常值检查的列
    for col in outlier_check_list:
        # 若数据集中存在需要进行检查的列，则采用对应的处理方法
        if col in df_columns_list:
            print(f'数据集中存在“{col}”，是否进行异常值处理（Y/N)?')
            result = input_to_boolean()

            if result is True:
                # 选择对应的处理方法
                if col == '作答时间':
                    aimed_col = df['作答时间'].str.replace('小时', ':')
                    aimed_col = aimed_col.str.replace('分', ':')
                    aimed_col = aimed_col.str.replace('秒', '')

                    aimed_col = aimed_col.str.split(':')
                    l = []
                    for i in aimed_col:

                        if i[-1] == '':
                            i[-1] = 0
                        i = list(map(int, i))

                        if len(i) == 3:
                            l.append((i[0] * 60 + i[1] + i[2] / 60))
                        elif len(i) == 2:
                            l.append((i[0] + i[1] / 60))
                        elif len(i) == 1:
                            l.append(i[0] / 60)

                    aimed_col = DataFrame({'作答时间': df['作答时间'], '标准化作答时间（分钟）': l})
                    cleaned_outlier_df['标准化作答时间（分钟）'] = aimed_col['标准化作答时间（分钟）']

                    print(aimed_col)
                    print(aimed_col.describe())

                    mean = aimed_col['标准化作答时间（分钟）'].mean()
                    std = aimed_col['标准化作答时间（分钟）'].std()

                    max = aimed_col['标准化作答时间（分钟）'].max()
                    min = aimed_col['标准化作答时间（分钟）'].min()
                    two_std_l = mean - 1.96 * std
                    two_std_r = mean + 1.96 * std

                    if max > two_std_r or min < two_std_l:
                        print('数据集作答时间存在极端值（95%置信区间）', 'avg=%.2f，std=%.2f，请手动处理！' % (mean, std))

                        # 返回异常作答时间所在行号
                        outlier_l = aimed_col['标准化作答时间（分钟）'][
                            aimed_col['标准化作答时间（分钟）'].values < two_std_l]
                        outlier_r = aimed_col['标准化作答时间（分钟）'][
                            aimed_col['标准化作答时间（分钟）'].values > two_std_r]
                        outlier_df = DataFrame({'标准化作答时间异常值（分钟）': pd.concat([outlier_l, outlier_r])})
                        outlier_index_list = outlier_df.index.values.tolist()
                        print(cleaned_outlier_df.loc[outlier_index_list])

                        # 处理异常值
                        print(f'\n是否删除作答时间异常行，即第{outlier_index_list}行（Y/N）？')
                        result = input_to_boolean()
                        if result is True:
                            cleaned_outlier_df = df.drop(outlier_index_list)
                        elif result is False:
                            print('是否需要手动删除指定行（Y/N）？')
                            result = input_to_boolean()
                            if result is True:
                                print('请输入需要删除的数据的【行号】（不是序号），若存在多个，以空格分隔')
                                outlier_index_list = list(input().split())
                                # 将字符串转换为数字
                                for i in range(len(outlier_index_list)):
                                    try:
                                        outlier_index_list[i] = int(outlier_index_list[i])
                                    except:
                                        print('非法输入！')
                                        quit()  # ======================================
                                # 删除指定行
                                cleaned_outlier_df = df.drop(index=outlier_index_list)

                            elif result is False:
                                quit()  # =======================================



                    else:
                        print('\n未检测到数据集作答时间存在极端值（95%置信区间）', 'avg=%.2f，std=%.2f，建议手动检查！' % (mean, std))

    print('\n异常值清洗完成！\n')

    print(f'数据集描述：\n{cleaned_outlier_df.describe()}\n')
    print(f'请人工检查清洗后数据集：\n{cleaned_outlier_df}\n')

    return cleaned_outlier_df

# test
cleaned_NaN_df = clean_NaN(ori_data)
cleaned_duplication_df = clean_duplication(cleaned_NaN_df)
cleaned_outlier_df = clean_outlier(cleaned_duplication_df)
# cleaned_outlier_df = clean_outlier(ori_data)
