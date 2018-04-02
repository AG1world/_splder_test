from django.conf.urls import url
from blog import views

urlpatterns = [

    # 无命名分组
    url(r'^article/(\d{4})$', views.article),
    # 有名分组
    url(r'^article/(?P<year>\d{4})/(?P<month>\d{2})', views.article_1),
    # 为url设置别名
    url(r'^register/', views.register, name='reg'),
    url(r'^now_time/', views.now_time, ),
    url(r'^add/', views.add, ),
    url(r'^delete/', views.delete,),
    url(r'^update/', views.update, ),
    url(r'^query/', views.query, ),
    url(r'^index/', views.index, ),

    url(r'^login/', views.login, ),
    url(r'^cookie_test/', views.cookie_test, ),
    url(r'^logout/', views.logout, ),
]