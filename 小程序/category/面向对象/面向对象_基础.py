

# 神码为类--- 具有某一类打相似特征和动作(功能)


# 函数实现面向对象

def dog():

    def jiao(dog_1):     # 这个dog是通过调用外层函数的返回值
        print('%s在叫'%dog_1['name'])
    def chishi(dog_1 ):
        print('%s在吃屎'%dog_1['type'])

    dog1 = {
        'name':'高无菌',
        'gender':'母',
        'type':'腊肠',
        'jiao':jiao,
        'chishi':chishi

    }
    return dog1   # 返回俩个函数的

res = dog()
res['jiao'](res)   # res得到的是dog函数的返回值即 dog1字典和俩个函数对象
print(res)


# def dog(name,gender,type):
#
#     def jiao(dog):
#         print('%s在叫'%dog['name'])
#     def chishi(dog ):
#         print('%s在吃屎'%dog['type'])
#
#     dog1 = {
#         'name':name,
#         'gender':gender,
#         'type':type,
#         'jiao':jiao,
#         'chishi':chishi
#
#     }
#     return dog1
#
# res = dog('菜鸡2号','母','中华田园狗')
# res['jiao'](res)
# res['chishi'](res)
#
# res1 = dog('菜鸡23号','母','日八田园狗')
# res1['jiao'](res1)
# res1['chishi'](res1)


# def dog(name,gender,type):
#
#     def jiao(dog):
#         print('%s在叫'%dog['name'])
#     def chishi(dog ):
#         print('%s在吃屎'%dog['type'])
#
#     dog1 = {
#         'name':name,
#         'gender':gender,
#         'type':type,
#         'jiao':jiao,
#         'chishi':chishi
#
#     }
#     return dog1
#
# res = dog('菜鸡2号','母','中华田园狗')
# res['jiao'](res)
# res['chishi'](res)
#
# res1 = dog('菜鸡23号','母','日八田园狗')
# res1['jiao'](res1)
# res1['chishi'](res1)


# 最终版优化


def dog(name, gender, type):

    def jiao(dog):
        print('%s在叫'%dog['name'])
    def chishi(dog ):
        print('%s在吃屎'%dog['type'])
    def init(name,gender,type):
        dog1 = {
            'name':name,
            'gender':gender,
            'type':type,
            'jiao':jiao,
            'chishi':chishi

        }
        return dog1   # 返回一个函数引用对象
    res = init(name,gender,type)
    return res      #返回一个字典

res = dog('菜鸡2号','母','中华田园狗')
res['jiao'](res)
res['chishi'](res)

res1 = dog('菜鸡23号','母','日八田园狗')
res1['jiao'](res1)
res1['chishi'](res1)