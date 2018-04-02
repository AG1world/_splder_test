#1.  斐波契纳数列1,2,3,5,8,13,21............
# 根据这样的规律，编程求出400万以内最大的斐波契纳数,并求出它是第几个斐波契纳数。
import copy


def feibo(num,a=1,b=2):
    count = 0
    max =0
    if num < 3:
        max = num
        count =num
    else:
        # 当num=3开始
        count = 2
        while max<num:
            max=a+b
            # 捕捉最后一次换数大于num,将返回max和count
            if max>num:
                max = max - a
                return  max,count
            a,b =b,max
            count +=1
        return max,count



# 使用4000000肯定不能使用递归,递归太占内存
a,b = feibo(4000000)
print(a,b)

# a,b = feibo(4)
# print(a,b)

def bofe(n):
    a = 0
    b = 1
    i = 0
    while i < n:
        i += 1
        a, b = b, a+b
    print(a, b)
#
bofe(40)


'''
【题目】2
上机编程实现以下功能：
dicta = {"a":1,'b':2,'c':3,'d':4,'f':'hello' }
dictb = {“b':3,'d':5,'e':7,'m':9,'k':'world'}
要求写一段代码，实现两个字典的相加，不同的key对应的值保留，相同的key对应的值相加后保留,如果是字符串就拼接，如上示例得到结果为：
dictc = {“a':1,'b':5,'c':3,'d':9,'e':7,'m':9,'f':'hello','k':'world'}


'''
a = {"a":1,'b':2,'c':3,'d':'m','f':'hello' }
b = {'b':3,'d':5,'e':7,'m':9,'f':'world'}

def new_dict(a,b):
    d = {}
    c = copy.deepcopy(a)
    a.update(**b)
    for key in c.keys():
        # 判断 字数与字母相加情况
        if str(a[key]).isdigit() and not str(c[key]).isdigit() or str(c[key]).isdigit() and not str(a[key]).isdigit():
            a[key] = str(a[key]) + str(c[key])
        else:
            # 当是全数字就可以转int型
            a[key] = int(str(a[key] + c[key])) if str(a[key] + c[key]).isdigit() else str(a[key] + c[key])
    d = a
    return d

d = new_dict(a,b)
print(sorted(d.items(),key = lambda a:a[0]))

# c = copy.deepcopy(a)
# a.update(**b)
# for key in c.keys():
#     # 判断 字数与字母相加情况
#     if str(a[key]).isdigit() and not str(c[key]).isdigit() or str(c[key]).isdigit() and not str(a[key]).isdigit():
#         a[key] = str(a[key])+ str(c[key])
#     else:
#         # 当是全数字就可以转int型
#         a[key]=int(str(a[key]+c[key])) if str(a[key]+c[key]).isdigit() else str(a[key]+c[key])
# print(a)



# dicta = {"a": 1, "b": 2, "c": 3, "d": 4, "f": "hello"}
# dictb = {"b": 2, "d": 5, "e": 7, "m": 9, "k": "world"}
#
# def add_dict(dicta, dictb):
#     dictc = {}
#     for i in dicta.keys():
#         if i not in dictb.keys():
#             dictc[i] = dicta[i]
#         else:
#             dictc[i] = dicta[i] + dictb[i]
#         for j in dictb.keys():
#             if j != 1:
#                 dictc[j] = dictb[j]
#
#     print(sorted(dictc.items(),key = lambda a:a[0]))
#
# add_dict(dicta, dictb)
# [('a', 1), ('b', 2), ('c', 3), ('d', 5), ('e', 7), ('f', 'hello'), ('k', 'world'), ('m', 9)]
# [('a', 1), ('b', 2), ('c', 3), ('d', 5), ('e', 7), ('f', 'hello'), ('k', 'world'), ('m', 9)]