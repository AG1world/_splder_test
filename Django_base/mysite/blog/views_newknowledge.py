# dajngo 请求周期之 FBV与CBV

#FBV就是url映射常见的试图函数

#CBV就是类视图继承基类View调用dispatch()分发不同请求方式的视图函数,相当于一个媒介,
# 同时url解析时就会调用url,我们如果在任何请求情况下都需要处理,可以通过继承基类修改dispatch()方法来实现功能
from django.http import HttpResponse
from django.views.generic import View


class CBV(View):
    def dispatch(self,request,*args,**kwargs):
        # 通过调用父类的dispathc(),同时添加功能<例如任何请求下的验证登录功能>
        re = super(CBV, self).dispatch(self,request,*args,**kwargs)
        return re

    def get(self):
        pass
    def post(self):
        # 设置响应体
        ret = HttpResponse('nihao')
        # 设置响应头
        ret['name'] = '你好'
        # 设置cookies
        ret.set_cookie('name','chen')
        return ret



