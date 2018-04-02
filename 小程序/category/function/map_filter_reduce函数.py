# map()方法
#将列表中原来的元素进行处理,得到的元素个数及位置与原来一样
# 1.方法构造
from functools import reduce
def map_test(func,lst):
    pass

# 2.使用
res = map(lambda x:x**2, [1, 3, 5, 7 ])
print(list(res))




# filter()方法
# 遍历列表,将适合的值(条件返回True)进行重新组合
# 1.方法构造
def filter_test(func,lst):
    pass

# 2.使用





# reduce()方法---->reduce(pa=func, pa2=seq,init=None,[num])
# 处理列表,将列表合并
# 1.方法构造
def reduce_test(func,lst):
    # 我们应该支持用户自己传入初始值
    def reduce_test(func, array, init=None):
        l = list(array)
        if init is None:
            res = l.pop(0)
        else:
            res = init
        for i in l:
            res = func(res, i)
        return res


# 2.使用
num_1 = [1, 2, 3, 100]
print(reduce(lambda x,y:x+y, num_1,1))
print(reduce(lambda x,y:x+y, num_1))