# 算法第一天
import time

# star_time = time.time()
# for a in range(1001):
#     for b in range(1001):
#         for c in range(1001):
#             if a + b + c == 1000 and a**2 + b**2 == c**2:
#                 print(a,b,c)
# end_time = time.time()
# print(end_time-star_time)


# Python内置类型性能分析

import timeit

# 模式class timeit.Timer(stmt='pass', setup='pass', timer=<timer function>)
# 运行直接运行的代码
# timer1 = timeit.Timer(stmt='print("xx")')
# print(timer1.timeit(100))

# 运行需要条件的语句
# timer2 = timeit.Timer(stmt='print(n)',setup='n=18')
# print(timer2.timeit(3))

# 调用函数
# def func():
#     print('xxxx')
# 将当前运行文件中函数加载到测试性能环境中
# timer3 = timeit.Timer('func()','from __main__ import func')
# print(timer3.timeit(5))

# list操作测试
# 列表相加
def func1():
    lst1 = []
    for i in range(1000):
        lst1 = lst1 + i
        lst1 = lst1 + [i]
# 列表appded

def func2():
    lst1 = []
    for i in range(1000):
       lst1.append(i)
# 列表生成式

def func3():
    lst1 = [i for i in range(1000)]
# 列表list(range())
def func4():
    lst1 = list(range(1000))

timer1 = timeit.Timer('func1','from __main__ import func1')
print(timer1.timeit(number=5000000))

timer2 = timeit.Timer('func2','from __main__ import func2')
print(timer2.timeit(number=5000000))

timer3 = timeit.Timer('func3','from __main__ import func3')
print(timer3.timeit(number=5000000))

timer4 = timeit.Timer('func4','from __main__ import func4')
print(timer4.timeit(number=50000))







