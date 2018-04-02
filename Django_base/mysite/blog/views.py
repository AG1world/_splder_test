from django.db.models import F
from django.db.models import Q
from django.shortcuts import render,HttpResponse, redirect

# Create your views here.
import time

from django.template import Template,Context

from django.db.models import Avg,Min,Sum,Max

def show_time(req):
    time1 = time.ctime()
    # 必须返回的httpresponse对象
    # return HttpResponse('hello:%s'%time1)

    # 返回封装的模板
    # return render(req, 'index1_1.html',locals())
    return render(req, 'index1_1.html',{'time1':time1})


def article(req,y):
    return HttpResponse('年份:%s'%(y))


# 命名分组,传入参数必须与url中的参数相对应
def article_1(req,year,month):
    return HttpResponse('年份:%s, 月份:%s'%(year, month))


def register(request):
    # 获取 GET提交的参数
    if request.method == 'POST':
        print(request.POST.get('name'))
        print(request.POST.get('age'))
        return HttpResponse('Succes')

    return render(request,'register.html')


def now_time(req):
    t1 = time.ctime()
    # 同一模板多个上下文,应先建立模板,再调用render()方法渲染

    #----------------------------原生模板的应用----------------------------------------------
    # now  = time.time()
    # temp = Template(('<html><body>现在时刻是:<h1 style="color:red">{{current_date}}</h1></body></html>')
    # # 或者使用get_template('datetime.html')
    # c = Context({'current_date':now})
    # html = temp.render(c)
    # return HttpResponse(html)

    return render(req,'now_time.html',locals())

# 图书类打增删改查
from blog.models import *

def index(req):

    return render(req,'index.html')


def add(req):
    # <添加字段时必须将数据添全>
    # 1. 创建一条记录就是创建一个对象
    # b = Book(name='天下第一',author='梁羽生',price=58,pub_date='1965-12-13')
    # b.save()
    # 2. 更好用
    Book.objects.create(name='天龙八部',author='金庸',price=38,pub_date='1965-12-13')

    return HttpResponse('添加成功')


def delete(req):
    Book.objects.filter(id=1).delete()
    return HttpResponse('删除成功')


def update(req):
    # 1. update()效率更高
    Book.objects.filter(id=1).update(price=58)

    # 2. save() 修改对应记录所有字段
    # b = Book.objects.get(id=1)
    # b.price = 28
    # b.save()
    return HttpResponse('修改成功')


def query(req):
    # book_list = Book.objects.all()
    # print(book_list)  # 获取对象列表
    # print(book_list[0])  # 获取对象
    # book_list = Book.objects.filter(id=2)
    # book_list = Book.objects.all()[::2]
    # book_list = Book.objects.all()[::-1]
    # book_list = Book.objects.first()
    # book_list = Book.objects.last()
    # book_list = Book.objects.get(author='周星驰') # 获取值必须只能有一个
    # re1 = Book.objects.filter(author='周星驰').values('name','price') #[{'name': '功夫'}]--键值对的形式
    #
    # re2 = Book.objects.filter(author='周星驰').values_list('name','price') # [('功夫',)]--元祖打形式
    # 取反向的数据
    # re3 = Book.objects.exclude(id=2).values('id','name','price')
    # print(re1)
    # print(re2)
    # print(re3)
    # 对name及price去重

    # book_list = Book.objects.all().values('name','price').distinct()
    # print(book_list)


    # 万能的双下划线__
    # book_list =Book.objects.filter(price__gt=50)
    # book_list =Book.objects.filter(name__contains='天下')  #name` LIKE BINARY '天下%'
    # book_list =Book.objects.filter(name__icontaons='Py') # 不区分大小写
    # book_list =Book.objects.filter(id__gte=3,id__lte=7)
    # book_list =Book.objects.filter(price__in=[22,58])   # 选择 22,58 取值
    # book_list =Book.objects.filter(price__range=[22,53])  # 范围取值
    # book_list =Book.objects.exclude(price__in=[22,])  # 反向取值
    # book_list =Book.objects.filter(name__startswith='天下')  # 开始/结束 endwith
    # 通过在start_with 与 endwith  前面加i  不区分大小写{istartwith, iendwith}


    # 多对多查询
    # 任务1: 查询alex 写几本书及价格
    # re = Book.objects.filter(authors__au_name='alex').values('name','price')
    # print(re)
    # 原生sql语句查询
    # 'ELECT `blog_book`.`name`, `blog_book`.`price` FROM `blog_book`
    # INNER JOIN `blog_book_authors` ON ( `blog_book`.`id` = `blog_book_authors`.`book_id` )
    # INNER JOIN `blog_author` ON ( `blog_book_authors`.`author_id` = `blog_author`.`id` )
    # WHERE `blog_author`.`au_name` = 'alex' LIMIT 21; args=('alex',)


# 聚合查询
    # 查询出书的平均价格
    # re1  =  Book.objects.all().aggregate(Avg('price'))
    # print(re1) # {'price__avg': 23.0}

    # 给查询结果命名
    # re2  = Book.objects.aggregate(price_min1 = Min('price'),price_max = Max('price'))
    # print(re2)

    #--分组查询--对每个作者[对作者对象按着名字分组]出版书籍的价格总计   annotate
    # re3 = Book.objects.values('authors__au_name').annotate(Sum('price'))
    # print(re3)

    # 求每个出版社 price最低的书籍
    # re4 = Publish.objects.values('name').annotate(Min('book__price'))
    # print(re4)


    # 查询之 Q与F   F()是直接对字段的操作;使用查询条件的值,专门取对象中某列值的操作
    # re1  = Book.objects.filter(name__contains='p')
    # print(re1)
    # re2 = Book.objects.filter(name__contains='python基础').update(price=price+1)
    # re2 = Book.objects.filter(name__contains='python基础').update(price = F('price')+1)
    # print(re2)

    # Q 组合查询,通过逻辑关系表示不同的条件  ~Q() 非
    # re3 = Book.objects.filter(Q(name__contains='python')|Q(price__gte=23)&~Q(publish__name__contains='机械'))
    # print(re3)

     # 在生成querySet对象,惰性求值,只有使用时才查询数据库--提升性能
    # queryset  在重复执行相同语句会使用缓存,除非重新赋值


    # 缓存和iterator()使用   前者用于大量重复查询;iterator()用于数据量大




    # return render(req,'index.html',{'book_list':book_list})
    return render(req,'index.html')


# 通过设置cookie和session来限制用户直接访问cookie_test 页面
# 总结:cookie与色三思哦你实现了http协议无状态请求的缺陷,cookie是服务器端在浏览器第一次访问后发送一个cookie,
# 来记录 浏览器的身份,当数据提交时,也会请求中将cookie一并发送给服务器,服务器便能够识别浏览器身份,由于cookie数据大小
# 限制(4M)和浏览器本地存储不够安全,便引入session已键值对形式来记录 ,通过sessionid即为信息的键,也就是访问数据的
#钥匙,将sessionid 作为cookie发送给浏览器,从而更安全
"""
COOKIES {'sessionid': 'a4noop6zxxfxsnpz1vohtiuc4v4ko6ni'}
Session <django.contrib.sessions.backends.db.SessionStore object at 0x7fc0aae4ff28>

"""

def login(req):
    print('COOKIES',req.COOKIES)
    print('Session',req.session)   # 得到一个session对象
    if req.method=='POST':
        name = req.POST.get('user')
        pwd = req.POST.get('pwd')
        if name =='yuan' and pwd =='123':
            #当条件满足时,设置cookie状态

            # ret = redirect('/blog/cookie_test/')
            # # cookie将para1 作为键,para2为大字典的值
            # ret.set_cookie('username',{'is_login':True})
            # return ret   # 设置cookie值时记得返回

            #通过cookie与session操作session字典对象
            req.session['is_login'] = True
            req.session['user']  = name
            return redirect('/blog/cookie_test')
    return render(req,'login.html',locals())



def cookie_test(req):
    # if req.COOKIES.get('username',None):
    #     name = req.COOKIES.get('username',None)
    #     return render(req,'cookie_test.html',locals())
    is_login = req.session.get('is_login',False)
    if is_login:
        name = req.session.get('user')
        return render(req,'cookie_test.html',locals())
    else:
        return redirect('/blog/login/')

def logout(req):
    ''' 注销就是将存储的session删除'''

    # 当is_login字典不存在会出现key_error,需要加异常捕获
    try:
        del req.session['is_login']
        print(req.session.get('is_login'))
    except:
        pass
    return redirect('/blog/login/')
