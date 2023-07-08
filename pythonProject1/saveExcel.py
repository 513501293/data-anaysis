# Date: 2023/06/28

import pandas as pd
from pandas import DataFrame

""" 保存数据至excel文件 """

data = DataFrame({'ID': [1, 2, 3, 4, 5,6],
                'User': ['A', 'B', 'C', 'D', 'E','F']})

path = r'/Users/yiruwong/Desktop/testfile.xlsx'


def save_excel(df, file_path, sheetname):

    with pd.ExcelWriter(file_path, mode='a', if_sheet_exists='new') as writer:
        df.to_excel(writer, sheet_name=sheetname)


save_excel(data, path, 'Sheet5')
save_excel(data, path, 'Sheet7')
