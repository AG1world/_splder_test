#生成器
# 在在函数中使用yield
# 列表生成式将中括弧换成()

# yield 在读取大文件时通过每次去一次值来完成大文件的读取



# 1. 定义函数,求出文件中population总和
"""
{'name':'北京','population':10000}

{'name':'上海','population':20000}

{'name':'广州','population':30000}

{'name':'深圳','population':40000}

"""
import time


def diaocha(file_name):
    # with open('人口信息.txt','r',encoding='utf-8') as f:
    with open(file_name) as f:


        # lst = []
        # for i in f:
        #
        #     l = eval(i)
        #     lst.append(l['population'])
        # res = sum(lst)
        res = sum(eval(i)['population'] for i in f)
        return res

res = diaocha('人口信息.txt')
print(res)
# sum()pa 为可迭代对象
# res = sum(eval(i)['population']for i in f)

# 2. 求每次获取的人口信息
def diaocha1(file_name):
    # with open('人口信息.txt','r',encoding='utf-8') as f:
    with open(file_name) as f:
        for i in f:

            l = eval(i)
            res = l['population']
            yield res
res1 = diaocha1('人口信息.txt')
print('北京人口:%s'% res1.__next__()  )
print(res1.__next__())

# 生成器展示生产者消费者模式




def consumer(name):
    '''
    吃包子
    :return:
    '''
    print('我是[%s]准备吃包子'% name)
    while True:
         baozi = yield
         time.sleep(1)
         print('%s开始吃%s' % (name,baozi))

def productor():
    '''
    生产者 产生包子,将包子返回给消费者
    :yield:
    '''
    c1 = consumer('高无均')
    c2 = consumer('高无')
    c1.__next__()
    c2.__next__()
    for i in range(10):
        time.sleep(1)
        c1.send('--包子%s'% i)
        c2.send('--包子%s'% i)

productor()


# 生成器:当遇见yield时,只有激活生成器通过 next(),__next__(),send()三种方法激活,才能运行yield
# 后面打程序,当使用send()方法时,不能第一次激活生成器使用,前面必须调用一次next()方法