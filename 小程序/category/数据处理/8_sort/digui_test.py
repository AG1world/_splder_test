# import sys
##修改递归的最大深度限制
# sys.setrecursionlimit(1500)  # set the maximum depth as 1500
#
#
# def recursion(n):
#     if (n <= 0):
#         return
#     print( n)
#
#     recursion(n - 1)
#
#
# if __name__ == "__main__":
#     recursion(1200)


# 递归

# 1. 阶乘函数 !5 = 5*(4)*(3)*(2)*(1)
# n*(n-1)*(n-2)*(n-3)*(n-4) ....1
def jiechegn(n):
    if n == 1:
        return 1
    else:
        print('------------',n)
        return n * jiechegn(n - 1)



result = jiechegn(6)
print(result)


# 2. 斐波那契数列计算
# demo: 1, 1, 2, 3, 5, 8, 13
# 思想：当第一个位置和第二个位置等于1，第n个位置值,等于n-2和n-1的和
# 解决问题：求斐波那契数列第几个位置值
def febo(n):
    # '斐波那契额数列'
    # 写出递归结束条件
    if n == 1 or 2 == n:
        return 1
    else:
        return febo(n - 1) + febo(n - 2)
        # f(2)[1] +f(3)[1+1]


result = febo(5)
print(result)
