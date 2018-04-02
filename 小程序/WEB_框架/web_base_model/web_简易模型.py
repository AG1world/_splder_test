


from wsgiref.simple_server import   make_server

# def application(environ, start_response):
#     # 服务器将请求信息打包成字典打的形式
#     print(environ)
#     # 设置请求头
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     # 传入的字节串
#     return [b'<h1>hello world</h1>']
#
# # 创建的httpd 对象通过对接收的请求通过application函数进行处理
# httpd = make_server('', 8080, application)
# print('Server HTTP on port 8080...')
# # 开始监听http请求
# httpd.serve_forever()


#
# def application(environ, start_response):
#     # 服务器将请求信息打包成字典打的形式
#     print(environ['PATH_INFO'][1:].encode('utf8'))
#     # 设置请求头
#     start_response('200 OK', [('Content-Type', 'text/html')])
#     # 传入的字节串PATH_INFO
#     return [b'<h1>hello, %s</h1>' % (environ['PATH_INFO'][1:]).encode('utf8')]
#
# # 创建的httpd 对象通过对接收的请求通过application函数进行处理
# httpd = make_server('', 8081, application)
# print('Server HTTP on port 8081...')
# # 开始监听http请求
# httpd.serve_forever()

# 3-实现路由分发;动态获取时间
import time


def f1(req):
    print(req)
    print(req['QUERY_STRING'])
    f1 = open('test1.html','rb')
    data1 = f1.read()
    return [data1]

def f2(req):
    f2 = open('test2.html','rb')
    data2 = f2.read()
    return [data2]

def f3(req):
    f3 = open('test3.html', 'rb')
    data3 = f3.read()
    times = time.strftime('%Y-%m-%d %X', time.localtime())
    print('----------------', times)
    data3 = str(data3,'utf8').replace('{{time}}',str(times))
    return [data3.encode('utf8')]
def routers():
    '''
    创建路由
    :return: 得到一个元祖
    '''
    urlpatterns = (
        ('/yuan', f1),
        ('/alex', f2),
        ('/cur_time', f3),

    )
    return urlpatterns


def application(environ, start_response):

    print('>>>>>>>>>>>>>>>>>>>>>>开始')
    path = environ['PATH_INFO']
    # 设置请求头
    start_response('200 OK', [('Content-Type', 'text/html')])

    urlpatterns = routers()
    func = None
    for item in urlpatterns:
        if item[0] == path:
            func = item[1]
            break
    if func:
        return  func(environ)
    else:
        return ['<h1>404</h1>'.encode('utf8')]

# 创建的httpd 对象通过对接收的请求通过application函数进行处理
httpd = make_server('', 8082, application)
print('Server HTTP on port 8081...')
# 开始监听http请求
httpd.serve_forever()



