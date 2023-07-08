# Date：2023/07/05
""" 定义“问题”类
1. 问题分类	最上层的分类	人口学属性、购车行为等
2. 问题维度	抽象、简洁的调研角度	性别、购车动机、考虑因素等
3. 问题序号	问题在问卷中的顺序或序号	\
4. 问题描述	维度在问卷中面向用户的表现形式	您的性别、您在购车时考虑了以下哪些因素等
5. 必答/非必答	该问题是否为必答题或非必答题（决定数据清洗范围）	必答/非必答
6. 逻辑跳转	该问题是否与其它问题存在逻辑关系（影响是否必答）	跳题、跳转等
7. 题型	该问题的题目类型	单选、多选、排序、填空等
8. 选项/答案/数据	该问题获得的数据范围或数据	男女，‘fdsf’等
"""


class Question():
    # 实例对象动态添加属性可以使用__slots__来进行，但同时也仅限于__slots__的值内有的字段，直接给类增加属性不受此限制。
    __slots__ = ['classification', 'dimension', 'description', 'index', 'req_or_opt', 'logic', 'question_type',
                 'selections', 'data']

    def __init__(self, description: str):
        self.classification = None
        self.dimension = None

        self.description = description
        self.index = None
        self.req_or_opt = None
        self.logic = None
        self.question_type = None
        self.selections = None
        self.data = None

    def describe(self):
        print(f"题号：{self.index}\n"
              f"问题分类：{self.classification}\n"
              f"维度：{self.dimension}\n"
              f"题目：{self.description}\n"
              f"必答/非必答：{self.req_or_opt}\n"
              f"逻辑跳转：{self.logic}\n"
              f"题型：{self.question_type}\n"
              f"选项：{self.selections}\n"
              f"数据：{self.data}\n")


#q = Question('name?')
#q.req_or_opt = '必答题'
# if not hasattr(q, 'req_or_opt'):
#     setattr(q, 'req_or_opt', '必答题')

# print(q.description)
# print(q.req_or_opt)
#print(q.describe())
