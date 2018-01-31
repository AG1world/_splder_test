# 多线程_基础
import os
import threading, time


def loop():
    # 线程中 查看当前的线程,使用threading.current_thread()
    print('this is sub_thread{}'.format(threading.current_thread()) )

    num =10
    # 枚举法 第二位参数是遍历的序号
    for i,m in enumerate(range(num)):
        time.sleep(2)
        print('这是第{}个'.format(m))


# t = threading.Thread(target=loop)

if __name__ == '__main__':
    print('this is main_thread{}'.format(threading.current_thread()))
    for i in range(3):
        t = threading.Thread(target=loop)
        t.start()



