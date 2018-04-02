from twisted.internet import reactor    # 事件循环,内部是一个while True(终止条件为,所有的socket都已经移除)

from twisted.web.client import getPage    # socket 对象(如果下载完成,自动从事件循环中移除)

from twisted.internet import defer   # defer.Deferrer 特殊的socket对象,不送请求<不会发送请求, 手动移除>

# 创建socket,利用getPage
# 将socket添加到时间循环
# 开始事件循环,内部自动发送请求,并接受响应,当所有的socket请求完成后,终止事件循环




# 创建socket,利用getPage
# def response(content):
#     print(content)
#
# def task():
#
#     url = 'http://www.baidu.com'
#     # d也是特殊打deferred对象
#     d = getPage(url)
#     d.addCallback()

#################################

# 创建socket,利用getPage
# 将socket添加到时间循环
# 开始事件循环

# def response(content):
#     print(content)
#
# @defer.inlineCallbacks
# def task():
#
#     url = 'http://www.baidu.com'
#     # d也是特殊打deferred对象
#     d = getPage(url.encode())
#     d.addCallback(response)
#
#     yield d
# def done(*args,**kwargs):
#     reactor.stop()
#
# # 返回得到的socket
# d = task()
#
# # 监听socket执行情况
# dd = defer.DeferredList([d,])
#
# # 执行情况
# # dd.addCallback()
# # dd.addErrback()
#
# # 监听成功或者失败,参数是执行事件监听结束的引用
# dd.addBoth(done)
#
# # 添加到时间循环中
# reactor.run()


################################
count = 0
def response(content):
    global count
    count += 1

    if count ==3 :
        _close.callback(None)
    print(content)

_close = None
# 俩个task有俩个close() 此处只有一个,所以被挂起
@defer.inlineCallbacks
def task():

    url = 'http://www.baidu.com'
    # d也是特殊打deferred对象
    d1 = getPage(url.encode())
    d1.addCallback(response)

    url = 'http://www.51job.cn'
    # d也是特殊打deferred对象
    d2 = getPage(url.encode())
    d2.addCallback(response)

    url = 'http://www.jd.com'
    # d也是特殊打deferred对象
    d = getPage(url.encode())
    d.addCallback(response)

    global _close

    _close = defer.Deferred()
    yield _close




def done(*args,**kwargs):
    reactor.stop()

# 返回得到的socket
spider1 = task()
spider2 = task()
# 监听socket执行情况
dd = defer.DeferredList([spider1, spider2])

# 监听成功或者失败,参数是执行事件监听结束的引用
dd.addBoth(done)

# 添加到时间循环中
reactor.run()