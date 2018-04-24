from django.template import Library


# 创建register对象,且对象不能修改名字,para1=标签过滤第一值,另外为第二值
register = Library()

# 使用装饰器装饰自定义的过滤器,函数必须有返回值
@register.filter
def mod(num,a):
    return num%a


# 取余数
print(3%3)
