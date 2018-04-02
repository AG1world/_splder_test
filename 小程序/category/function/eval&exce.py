#1、语法
# eval(str,[,globasl[,locals]])
# exec(str,[,globasl[,locals]])

#2、区别
#示例一：
s='1+2+3'
print(eval(s)) #eval用来执行表达式，并返回表达式执行的结果
print(exec(s)) #exec用来执行语句，不会返回任何值
'''
6
None
'''

#示例二：
print(eval('1+2+x',{'x':3},{'x':30})) #返回33
print(exec('1+2+x',{'x':3},{'x':30})) #返回None

# print(eval('for i in range(10):print(i)')) #语法错误，eval不能执行表达式
print(exec('for i in range(10):print(i)'))



###加深印象,eval可以执行计算和表达式,不能执行语句 <1+2 , func()>
### exec() 可以执行语句---<for if else>