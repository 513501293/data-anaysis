# Date: 2023/07/02
""" 创建问题类

@param
dimension as str：问卷问题/维度
question_type as str：问题类型
data as df：问题的数据
"""

import pandas as pd
from pandas import DataFrame


class Question:

    def __init__(self, dimension, question_type):
        self.dimension = dimension
        self.question_type = question_type
        #self.data = data

    def show(self):
        print(self.dimension+',', self.question_type)


# test
#df = DataFrame({'姓名（填空）': ['1', '2', '3']})
#a = Question('姓名', '填空', df)
#a.show()
