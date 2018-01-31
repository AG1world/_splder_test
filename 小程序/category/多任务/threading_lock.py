# 多线程功 锁使用

# 出现的原因: 由于python高级语言,解释器运行时会将一个表达式按照多步骤分解,
# 多线程的运行,导致某些线程运行中断后,修改后的变量导致运算结果发生异常
# 创建2个线程,运行一个a的计算,执行10万次找到a! = 0情况
import threading


# a = 0
# def func1(n):
#     global a
#     a = n+a
#     a = a-n
#     # assert a != 0, '抛出异常'
#     if a != 0 :
#         print('------------------------------',a)
# def func2(n):
#     for i in range(1000000):
#         func1(n)
#
# if __name__ == '__main__':
#
#     t1= threading.Thread(target=func2,args=(1,))
#     t2 = threading.Thread(target=func2,args=(9,))
#     t1.start()
#     t2.start()


# lock 限制仅一个线程在同一时间对变量的修改

# 1. 实例化锁的对象
lock  = threading.Lock()
a = 0
def func(n):
    global a
    # 2. 线程获得锁
    lock.acquire()
    a  = n + a
    a = a - n
    # 3. 线程释放锁
    lock.release()
    if a != 0:
        print('------------------------------',a)
def func_lock(n):

    for i in range(1000000):
        func(n)

if __name__ == '__main__':
    t1= threading.Thread(target=func_lock,args=(1,))
    t2 = threading.Thread(target=func_lock,args=(9,))
    t1.start()
    t2.start()



