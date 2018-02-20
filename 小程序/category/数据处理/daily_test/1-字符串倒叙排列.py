# 1. 写一个函数,输入一个字符串,返回倒叙列表的结果:如string_reverse('abcdef'),返回'fedcba'
# 多种方法实现
import random

str1 = 'abcdef'

#  1. 列表切片
def string_slice(str):
    return str[::-1]
l = string_slice(str1)
# print(l)

# 使用for循环从右向左输出
# 对于列表生成式和生成器:
    # 当生成式外面给的是括号就是生成器,给的[]是生成式及列表
def string_reverse1(str):
    # print(str[i]for i in range(len(str)-1,-1,-1))
    return ''.join(str[i]for i in range(len(str)-1,-1,-1))
l = string_reverse1(str1)
# print(l)

# 2. 将俩个列表升序合并,并去除重复元素

l1 = [2, 3, 8, 4, 9, 5, 6]
l2 = [22, 12, 3, 5]

# 将俩个列表通过集合去重,在排序
def func(l1, l2):
    # print(list(set(l1+l2)))
    return list(set(l1+l2))
func(l1,l2)

# 想法: 合并俩个列表,先去重再排序
def func2(l1, l2):
    '冒泡排序'
    l = l1 + l2
    n = len(l)

    for i in range(n-1):
        for j in range(n-1-i):
            if l[j] == l[j+1]:
                l.remove(l[j+1])
            elif l[j] > l[j+1]:
                l[j],l[j+1] = l[j+1], l[j]
    # print(l)
    return l

l = func2(l1, l2)
print(l)