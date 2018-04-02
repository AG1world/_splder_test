# 把一类食物打特征和动作整合到一起就是类,是一个抽象打概念
# 对象: 基于类而创建的一个具体的食物(具体存在的),也是特征和动作整合到一起




# 类就是将一类事物的特征和功能整合到一起(即将数据和动作嵌到一个结构里,得到一个对象系统,类是抽象打,对象是实例化类,具有自己打特征(属性)和功能(函数方法))


class Chinese:
    '说明文档'
    dang = '共产党'

    def suiditutan(self):
        print('岁走随吐')
    def dasheng():
        print('大声喧哗')

print(Chinese.dang)
print(Chinese.__dir__(1))  # dir(Chinese)  得到类的属性列表
print(Chinese.__dict__) # 产看类属性的字典

# 通过类.属性是通过 类属性的字典来调用属性和方法的

print(Chinese.__dict__['dang'])
Chinese.__dict__['dasheng']()
Chinese.__module__  # 类的所在模块


