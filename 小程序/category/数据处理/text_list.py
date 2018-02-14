import timeit
def func1():
    lst  =[]
    for i in range(5):
        lst += i

def func2():
    lst  =[]
    for i in range(5):
        lst.append(i)

timer = timeit.Timer('func1','from __main__ import func1')


timer = timeit.Timer('func2','from __main__ import func2')
print(timer.timeit(5000000000))
