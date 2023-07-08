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
print('List1: ', list1)
#print(dict1)


list2 = ['aA', '领克09', 'L9', 'dd', 'BB', None, 'EE']
brand2 = ['奥迪', '领克', '理想', '大众', '奔驰', None, '特斯拉']
dict2 =l_b(list2, brand2)
print('List2: ', list2)
#print(dict2)

#print('\n')

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
#print('All: ', all)
#print('\n')


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

#print('Matched: ', matched)
#print('Unmatched: ', unmatched)


# 计算未匹配的元素之间的匹配度，并保存为列表
pair_list = []
replaced = []
keep = []

for i in range(len(unmatched)):
    ratio_list = []
    max_ratio = 0
    for m in unmatched[i+1:]:
        ratio = difflib.SequenceMatcher(None, unmatched[i], m).quick_ratio()
        ratio_list.append(ratio)
        #print('Item: {:10} {:10} {:.2f}'.format(unmatched[i], m, ratio))

    if len(ratio_list) > 0 and max(ratio_list) > 0.5:
        max_ratio = max(ratio_list)
        loc = i + ratio_list.index(max_ratio) + 1
        # print('Item: {:10} {:10} {:.2f} {}'.format(unmatched[i], unmatched[loc], max_ratio,loc))
        if (len(unmatched[i]) > len(unmatched[loc])) and (unmatched[i] not in matched):
            matched.append(unmatched[i])
            keep.append(unmatched[i])
            replaced.append(unmatched[loc])
        elif (len(unmatched[i]) < len(unmatched[loc])) and (unmatched[loc] not in matched):
            matched.append(unmatched[loc])
            keep.append(unmatched[loc])
            replaced.append(unmatched[i])
        elif len(unmatched[i]) == len(unmatched[loc]):
            print('Check!')
        pair = unmatched[i] + '-' + unmatched[loc]
        pair_list.append(pair)




print('All: ', sorted(np.unique(all).tolist()))

print('\nPair List: ', pair_list)
print('Keep: ', keep)
print('Replaced: ', replaced)

unmatched = list(set(all) - set(matched) - set(replaced))
print('\nMatched: ', sorted(matched))
print('Unmatched: ', sorted(unmatched))

new_all = matched + unmatched
old_all = list1 + list2
old_all = [i for i in old_all if i is not None]
print('\nNew All: ', new_all)
print('Cleaned All: ', all)
print('Old All: ', old_all)

car = []
for i in new_all:
    for k in range(len(all)):
        if i == all[k]:
            car.append(old_all[k])
            break

print('\nFinal: ', car)


