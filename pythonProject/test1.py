import difflib
import numpy as np


# 匹配车型与厂商
def l_b(l, b):
    dict = {}
    k = 0
    for i in l:
        if k in range(len(b)):
            dict[i] = b[k]
        k +=1

    return dict

list1 = ['Aa', '09', 'B B', '理想L9', 'C2', 'dd']
brand1 = ['奥迪', '领克', '奔驰', '理想', None, '大众']
dict1 =l_b(list1, brand1)
print(dict1)


list2 = ['aA', '领克09', 'L9', 'dd', 'BB', None, 'EE']
brand2 = ['奥迪', '领克', '理想', '大众', '奔驰', None, '特斯拉']
dict2 =l_b(list2, brand2)
print(dict2)

print('\n')

# 统一字符串格式
def cleanListStr(list):
    cleanedList = []

    for item in list:
        if item is not None:
            # 将字符串全部转换成大写并去除空格
            item = item.upper().replace(' ', '')
            cleanedList.append(item)

    return cleanedList


# 汇总两个列表中的元素
all = cleanListStr(list1) + cleanListStr(list2)
print('All: ', all)
print('\n')


# 统计all中的词频
cntItem = {}
for i in all:
    if i in cntItem:
        cntItem[i] += 1
    else:
        cntItem[i] = 1

#print(cntItem)


# 分别提取匹配的与未匹配的元素
matched = []
unmatched = []
for d in cntItem:
    if cntItem[d] == 2:
        matched.append(d)
    elif cntItem[d] == 1:
        unmatched.append(d)

print('Matched: ', matched)
print('Unmatched: ', unmatched)


# 计算未匹配的元素之间的匹配度，并保存为列表
dict ={}
ratio_list = []
for i in range(len(unmatched)):
    for k in unmatched[i+1:]:
        ratio = difflib.SequenceMatcher(None, unmatched[i], k).quick_ratio()
        print('Item: {:10} {:10} {:.2f}'.format(unmatched[i], k, ratio))
        if ratio > 0.5:

            if len(unmatched[i]) > len(k):
                matched.append(unmatched[i])
                unmatched.remove(unmatched[i])
                unmatched.remove(k)
            elif len(unmatched[i]) < len(k):
                matched.append(k)
                unmatched.remove(unmatched[i])
                unmatched.remove(k)
            elif len(unmatched[i]) == len(k):
                print('Check!')

print('List1: ', sorted(cleanListStr(list1)))
print('List2: ', sorted(cleanListStr(list2)))

print('All: ', sorted(np.unique(all).tolist()))

print('Matched: ', sorted(matched))
print('Unmatched: ', sorted(unmatched))
