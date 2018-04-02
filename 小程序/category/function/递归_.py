# 非伯纳切数列 1 1
from functools import reduce
# is 不等于   ==

# def febo(n):
#     if n==2 or n==1:
#         return 1
#
#     return (febo(n-1)+febo(n-2))
#
# res = febo(8)
# print(res)
#

# 阶乘

# def jiecheng(num):
#     if num == 1:
#         return 1
#     return num *jiecheng(num-1)
#
# l1 = jiecheng(8)
# print(l1)
#
# l2 = reduce(lambda x,y:x*y, [i for i in  range(1,9)])
# l2 = reduce(lambda x,y:x*y, list(range(1,9)))
# print(l2)
#
# l3 = 1*2*3*4*5*6*7*8
# print(l3)


# 获取传入的起始值和结束值,得到范围内的被3或7整除的值

# 获取传入的起始值和结束值,得到范围内的被3或7整除的所有值之和
# 并返回调用者,符合条件个数及符合条件值之和

#   递归
# def s37(start,end,num = 0,sum1 = 0):
#     '递归方式完成'
#     if start ==end:
#         return num,sum1
#
#     if start % 3 ==0 or start % 7 ==0 :
#         num += 1
#         sum1 +=start
#     res = s37(start+1,end, num, sum1)
#     return res
# r,b = s37(1,7)
# print(r,b)

#   for循环

def s73(start,end):
    num = 0
    sum1 = 0
    for i in  range(start,end+1):
        if i %3 ==0 or i %7 == 0:
            print(i)
            num +=1
            sum1 +=i
    return num , sum1

r, b = s73(1,7)
print(r,b)