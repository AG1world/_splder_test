
# 告诉编译器这是全局变量a
global a

def set_value(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global a
    a = value

def get_value():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global a
    return a

# set_value(3)
# print(get_value())
#
# set_value(9)
# print(get_value())

name = '杠娘'
def weihou():
    name = '陈卓'
    def weiweihou():
        nonlocal name   # 指定上一级变量
        name = '冷静'
    weiweihou()
    print(name)

# print(name)
# weihou()
# print(name)

# 预期 杠娘 冷静 杠娘  binggo

# name = '杠娘'
# def weihou1():
#     name = '陈卓'
#     def weiweihou():
#         global name   # 指定上一级变量
#         name = '冷静'
#     weiweihou()
#     print(name)

# print(name)
# weihou1()
# print(name)

# 预期杠娘 陈卓 冷静

# 全局变量

a ={'name' :'xiaoming', 'class':1}
def bar(x):
    if x['name'] =='xiaoming':
        x['name'] ='xiaohua'
        print(x)
    else:
        print('OK')


bar(a)
print(a)