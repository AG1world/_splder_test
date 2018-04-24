

# 抽象类
# 抽象类只定义方法,不实现,继承的子类必须实现定义的方法
import abc
class Fruit(metaclass=abc.ABCMeta):

    @abc.abstractmethod  # 定义抽象方法
    def price(self):
        pass
    @abc.abstractmethod
    def color(self):
        pass

class Apple(Fruit):
    def price(self):
        print('价格是:12')

    def color(self):
        print('红色')


a = Apple()
a.price()
a.color()
