from django.shortcuts import render,HttpResponse
from app01.models import  Book
import datetime


# Create your views here.

def addbook(request):
    # 添加记录
    ## 方式一
    date = datetime.datetime.now()
    # book = Book(title='sanguoyanyui2',pub_date=date,price=100)
    # book.save()

    ## 方式二
    book = Book.objects.create(title='sanguoyanyui3',pub_date=date,price=300)
    print(book.title)
    print(book.pub_date)
    return HttpResponse('添加成功')

def select(request):

    # (1) all() ： 返回queryset对象
    # 查询所有Book对象的列表，
    # booklist = Book.objects.all()
    # print(booklist,type(booklist))
    # for book in booklist:
    #     print(book.title,book.price)

    # (2) filter(): 返回queryset对象
    # 查询满足某一条件的 Book对象列表
    # 查询某一本书
    # booklist = Book.objects.filter(price=100)
    # print(booklist[0].title)

    # (3) first()  laster() ：返回model对象
    # 查到返回对象，查不到  返回 None
    # book = Book.objects.first()
    # print(book.title)


    # (4) get(): 等同于fliter， 返回model对象，不是列表
    # 必须 得是  有且只有 一条符合条件的。
    # 少了报错，多了也报错。
    # book = Book.objects.get(price=300)
    # print(book.title)

    # (5) exclude : 排除符合条件的，返回 queryset对象(列表集合)
    booklist = Book.objects.exclude(price=300)
    print(booklist)

    # (6) order_by
    # 升序
    booklist = Book.objects.order_by("price")
    # 降序
    booklist = Book.objects.order_by("-price")
    # price 降序，如果有相等得  在按照 id升序排列
    booklist = Book.objects.order_by("-price","id")


    return HttpResponse('查询成功')