# 多进程使用
import os
from multiprocessing import Process

# 创建5 个进程,打印进程号

def subprocess(i):
    print('this is num{}, Runing {}'.format(i,os.getpid()))


if __name__=="__main__":
    print('this is Parent process %s' % (os.getpid()))
    for i in range(5):
        # 创建5 个进程
        p = Process(target=subprocess, args=(i,))
        # 开启进程
        p.start()
        p.join()
    print('this Process is end')
#
# from multiprocessing import Process
# import os
#
# # 子进程要执行的代码
# def run_proc(name):
#     print ('Run child process %s (%s)...' % (name, os.getpid()))
#
# if __name__=='__main__':
#     print ('Parent process %s.' % os.getpid())
#     p = Process(target=run_proc, args=('test',))
#     print ('Process will start.')
#     p.start()
#     p.join()
#     print ('Process end.')