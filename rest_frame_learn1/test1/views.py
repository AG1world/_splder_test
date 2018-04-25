from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
import json

from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt

# 视图函数中
@csrf_exempt
def users(req):
    l = ['gao','zhang']
    return HttpResponse(json.dumps(l))

# 设置一个基类,用来改写dispatch方法
class MyBaseView(object):

    def dispatch(self, request, *args, **kwargs):
        print('before')
        ret = super(MyBaseView, self).dispatch(request, *args, **kwargs)
        print('after')
        return ret

# 类视图中免除验证


class Students(MyBaseView,View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        ret = super(Students, self).dispatch(request, *args, **kwargs)
        return ret

    def get(self,*args,**kwargsrgs):
        print('GET')
        return HttpResponse('GET')


    def post(self,*args,**kwargsrgs):
        return HttpResponse('POST')
    def put(self,*args,**kwargsrgs):
        return HttpResponse('PUT')
    def delete(self,*args,**kwargsrgs):
        return HttpResponse('DELETE')



#封装实例
# class Request(object):
#     def __init__(self,obj):
#         self.obj  =obj
#     @property
#     def user(self):
#         return self.obj.authticate()
#
#
# class Auth(object):
#     def __init__(self,name,age):
#         self.name = name
#         self.age  =age
#
#     def authticate(self):
#         return True
#
#
# class APIView(object):
#     def dispatch(self):
#         self.f2()
#     def f2(self):
#         a = Auth('alex', 18)
#         req = Request(a)
#         print(req.user)
#
# obj = APIView()
# obj.dispatch()