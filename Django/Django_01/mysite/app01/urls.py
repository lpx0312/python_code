from django.contrib import admin
# Django 1.x的时候 都是 url，2.x后都是path，这里re_path 就是 正则匹配URI，re_path 是需要新添加的
from django.urls import path ,re_path
from app01 import views

urlpatterns = [
    # 匹配到第一个后 就停止，
    path('admin/', admin.site.urls),
    path('timer/', views.timer),
    re_path('^articles/2003/$',views.year2003),
    # re_path('^articles/\d{4}/$',views.year),


    # # 分组() 可以将分组中的内容 作为第二个参数传给视图函数
    # # 单分组
    re_path('^articles/(\d{4})/$', views.year),
    # # 多分组
    # re_path('^articles/(\d{4})/(\d{2})/$', views.year_month)

    # 有名分组
    re_path('^articles/(?P<year>\d{4})/(?P<month>\d{2})/$', views.year_month2)

    # URL分发

]
