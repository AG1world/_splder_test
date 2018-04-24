# dic = {'k1':1,'k2':2,'k3':'abc'}
#
# # 打印序号及key val值
# # enumerate(seq,[start=1])开始位置
# for i,v in enumerate(dic.items(),1):
#     print(i,v[0],v[1])
#
#
#
# for i,v in enumerate(dic.items()):
#     print(i,v[0],v[1])
#
#
#
#
# '''
# 1 k2 2
# 2 k1 1
# 3 k3 abc
# '''

# 反射的增删改查
class Test(object):
    name = 'andrew'
    def func(self):
        print('[%s]你真棒'% self.name)

s1 = Test()
# 查询属性
# print(hasattr(s1,'func'))

def test1(num):
    print('错误{}'.format(num))

#获取属性 当有对应的属性时就会获取,没有时则抛出异常,当有设置默认值就会获取默认值属性(字符串或者对象或者方法)
# print(getattr(s1,'name1',test1))
# s = getattr(s1,'name1',test1)
# s(1)

# 修改属性,可以设置 lambada函数或者函数名
setattr(Test, 'test1', test1)
q=hasattr(Test,'test1')
# print(q)
# print(Test.__dict__)

# 传参数

# 删除属性
delattr(Test,'name')
p = hasattr(Test,'name')
# print(p)
# print(Test.__dict__)


# print('---------------------------__item系列__')
class People(object):
    age = '18'

    def __init__(self, name):
        self.name = name


    def __getitem__(self, key):
        print('getitme已启动')
        return self.__dict__[key]


    def __setitem__(self, key, value):
        self.__dict__[key] = value
        print('setitem已启动')

    def __delitem__(self, key):
        print('delitem已启动')
        self.__dict__.pop(key)
p  = People('zhang')
# print(p.name)
# p['x']=10 # setitem已启动
# print(p['x'])# getitem已启动
# del p['x']
# p.country = 'china' # __setattr__ 启动
# print(p.__dict__)


# print('---------------------------__getattribute系列__')

class Parent:
    def __init__(self, name):
        self.name  = name

    # def __getattribute__(self, item):
    #     print('%s_,不管是正常还是异常我先执行'% item)
    #     # 异常需要抛出指定的类或者继承基类 BaseException
    #     raise AttributeError('调用非法属性,高不定')
        # raise '调用非法属性,高不定'



    def __getattr__(self, item):
        print('触发getattr')
        print('%s_, 异常问题,请放心我可以搞定' % item)

p1 = Parent('小在子')

# p1.age
#  执行顺序是 getattribute --> getattr --> 获取__class__ 父类属性,从上面顺序执行

print('------------str   与    repr---------------------------')

class School:
    def __init__(self,name,addr,type):
        self.name=name
        self.addr=addr
        self.type=type

    def __repr__(self):
        return 'School(%s,%s)' %(self.name,self.addr)
    # def __str__(self):
    #     return '(%s,%s)' %(self.name,self.addr)

# print(),str() 函数都是调用对象的__str__方法(obj.__str__())
# repr 主要用于交互式解释器(python原生ide),没有str方法会调用repr()

print(School)
s = School('gao','ShangHai','s')
print(s)

print('-----------------format自定制----------------------')

fmt_dict = {
    'ymd':'{0.year}_{0.month}_{0.day}',
    'dmy':'{0.day}/{0.month}/{0.year}',
    'mdy':'{0.month}-{0.day}-{0.year}',

}
class Date:
    '自定制日期格式'
    def __init__(self,year,month,day):
        self.year  = year
        self.month  = month
        self.day  = day

    def __format__(self, format_spec):
        if not format_spec or format_spec not in fmt_dict:
            format_spec = fmt_dict['ymd']
        fmt = fmt_dict[format_spec]
        return fmt.format(self)


d = Date(1998,10,1)
print(d.__format__('mdy'))