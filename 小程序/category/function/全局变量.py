
# 告诉编译器这是全局变量a
global a

def set_value(value):
    # 告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,而不是方法内部的局部变量.
    global a
    a = value

def get_value():
    # 同样告诉编译器我在这个方法中使用的a是刚才定义的全局变量a,并返回全局变量a,而不是方法内部的局部变量.
    global a
    return a

set_value(3)
print(get_value())

set_value(9)
print(get_value())