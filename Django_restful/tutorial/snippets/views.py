from django.http import HttpResponse

from django.shortcuts import render

# Create your views here.



def index(req):
    # return HttpResponse('OK')
    return render(req,'index_1.html')