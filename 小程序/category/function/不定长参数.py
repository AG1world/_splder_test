# args 接受列表,kwargs接受的是字典
# 参数 实参位置参数必须在行参的左边
# 参数间必须是一一对应的关系


def fun(x, *args, **kwargs):
    print(x)
    print(args,args[0])
    print(kwargs,kwargs.get('x'))
    print('-----------------')

    print(*args,args[0])
    print(kwargs)
    # print(**kwargs)

fun(1,3,2,4,y=1,z=2)

# * ** 是将参数拆包 ,关键字参数不能拆包
# **args 支持传入的是以列表的形式,可以为: None ,
# **kwargs 支持传入的参数为: k=v ,

#args 是打包 元祖打形式,kwargs是以{}字典的形式