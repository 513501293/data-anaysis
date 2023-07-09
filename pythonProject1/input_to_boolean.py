
# coding: utf-8

# In[1]:


""" 用户输入Y/N，返回boolean
根据用户输入的指令，返回相应值或动作
1. Y：True，N：False
2. EXIT：退出程序
3. 其他输入：报错并循环，重新输入

@param
command as str：用户输入的指令

@return 
boolean
"""


# In[1]:


def input_to_boolean():
    
    # 若其它输入，则开启循环
    while True:
        
        # 用户输入指令
        command = input().strip().upper()    # 格式化
        print('\n')
              
        # 判断指令，并执行相应动作
        if command == 'Y':
            return True
        elif command == 'N':
            return False
        
        # 退出程序
        elif command == 'EXIT':
            exit()
            print('已关闭程序')
            break
            
        # 错误输入
        else:
            print('输入错误，请重新输入！')
            continue


# In[4]:


# input_to_boolean()

