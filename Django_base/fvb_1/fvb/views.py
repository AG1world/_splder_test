from django.shortcuts import render

# Create your views here.


# 静态属性 @property
# 将类的函数属性通过装饰器修饰后,直接通过.函数名就可以执行方法,避免传参
# 可以获取实例属性和类属性
class House(object):
    def __init__(self,name,length,width):
        self.name = name
        self.length = length
        self.width = width
    @property
    def cal_area(self):
        area  = self.length * self.width
        return  area
h1 = House('xiaoming',20,5)
h2 = House('zhangsan',18,12)

# print(h1.cal_area)
# print(h2.cal_area)

# 类方法  @classmethod
# 需求:仅仅只需要通过类本身来调用方法,不需要实例(与对象无关)第一个参数为cls,第二个需要传递
class Country(object):
    tag = " I'm a Chinese "
    @classmethod
    def area(cls,m):
        real_area =m
        print('实际面积为:%s'% real_area)

# 静态方法 @staticmethod  与类和实力对象无关,不能调用类变量和实力变量(名义上的归属,类的工具包)
    @staticmethod
    def static():
        print('静态方法')
# Country.area(100)
# Country.static()
c = Country()
c.static()
"""
实例对象只有实例属性,调用的类属性,第一个参数是self


"""


# 选课系统  获取对应的学校和课程

# 学校对象定义
class School(object):
    def __init__(self,name,location):
        self.name = name
        self.location = location

    def zhaosheng(self):
        pass


# 定义课程对象

class Course(object):
    def __init__(self,name,price,period,school):
        self.name = name
        self.price = price
        self.period = period
        self.school = school

    def paike(self):
        pass


# 实例化校区
s1 = School('老男孩','北京')
s2 = School('黑马','南京')
s3 = School('先锋','天京')

msg = """
1  老男孩 北京
2  黑马   南京
3  先锋   天京

"""
while True:

    print(msg)
    menu = {
        1:s1,
        2:s2,
        3:s3,
    }
    choice = int(input('请输入你选择的校区编号:'))
    school_obj = menu[choice]
    name = input('请输入你选择的学习周期:')
    price = input('请输入你选择的课程价格:')
    period = '一年'


    c = Course(name,price,period,school_obj)
    print('您选择的是[%s]校区,[%s]课程'%(c.school.name,c.name))

'''
小思路:通过以字典对应的k-v形式来传递school对象,可以用在支付方式和生产开发模式的选择

pay_method = {
    1:'支付宝'
    2:'现金'
    3:'微信'

}
method = pay_method[key]
def  func(method):

'''