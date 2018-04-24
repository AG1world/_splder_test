from django.conf.urls import  url

from snippets import views

urlpatterns = [

    url(r'^', views.index),
]



#生成器实现feibo数列
#简陋版,不能进行for循环
# class feibo():
#     def __init__(self,a=1,b=1):
#         self.a = a
#         self.b = b
#     def __iter__(self):
#         pass
#     def __next__(self):
#         self.a, self.b = self.b, self.a+self.b
#         print(self.a)
#         return self.a
#
# f = feibo()
# print(f)
# f.__next__()
# f.__next__()
# f.__next__()
# f.__next__()
# f.__next__()

#完整版
#传入一个值,将符合的feibo数列举出来

# class Feibo:
#     def __init__(self,max):
#         self.a = 1
#         self.b = 1
#         self.max = max
#     # 返回迭代对象
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         # 记录之前的self.a值,当下次交换值大于max值就将fib返回
#         fib = self.a
#         self.a, self.b = self.b , self.a+self.b
#         if self.a > self.max:
#             raise StopIteration('没有值了')
#         # print(fib)
#         return fib
# f = Feibo(1000)
# f.__next__()
# f.__next__()
# f.__next__()
# f.__next__()
# f.__next__()
# for i in f:
#     print(i)