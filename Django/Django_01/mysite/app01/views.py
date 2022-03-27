from django.shortcuts import render,HttpResponse,redirect

# Create your views here.
import json
import datetime

def timer(request):
    # request: 请求对象
    '''



    '''
    print(request.method)  # 请求的方式
    print(request.GET)             # POST如果uri有参数，这里就是参数，<QueryDict: {'count': ['10']}> GET的话就是uri的参数
    print(request.POST)            # POST请求的body <QueryDict: {'name': ['lpx'], 'age': ['18']}>
    print(request.path)            # /timer/ uri但是不带，参数
    print(request.get_full_path()) # /timer/?name=lpx&abc=123 包含参数，没参数情况下是一样的。

    # 解析请求的内容
    # POST ： body 中含有  name=lpx age=18
    print(request.POST.get('name'))  # lpx
    # POST : 如果body中包含 两个相同的键 name=lpx name=wy
    print(request.POST.get('name')) # wy ， 默认get会返回最后一个值
    # 要想获取所有的可以使用getlist 获取列表

    if len(request.POST.getlist('name')) > 1:
        print('name参数不止一个')
        print(request.POST.getlist('name'))  # ['lpx', 'wy']

    print(request.get_port())  # 8000
    print(request.get_host())  # 127.0.0.1:8000
    print(request.user)  # AnonymousUser
    print(request.read())

    now = datetime.datetime.now()
    s = now.strftime("%Y/%m/%d %X")

    # 步骤：选中templates文件夹—>右键—>选择Mark Directory as Template Folder—>等待5秒
    return render(request, "timers.html",{"timers":s})
    # return HttpResponse(json.dumps({"result":"200"}))

# 不分组函数
def year2003(request):
    return HttpResponse('2003.....')

# 单分组函数
def year(request,year):
    return  HttpResponse("{0}年份的书籍".format(year))

# 多分组函数
def year_month(request,year,month):
    return HttpResponse('{0}年 {1}月 的书籍'.format(year,month))


def year_month2(request,year,month):
    return HttpResponse(':::{0}年 {1}月 的书籍'.format(year,month))


# action="http://127.0.0.1:8000/auth/" 认证的方法
def auth(requst):
    user = requst.POST.get('user')
    password = requst.POST.get('password')
    print('user:{0} password:{1}'.format(user, password))

    if user == 'lpx' and password=='123' :
        # 如果用户名密码正确，重定向302 ，没有相应体，有相应头，
        # 相当于 让浏览器 再次发个请求   http://127.0.0.1:8000/timer/

        # redirect 重定向 到 http://127.0.0.1:8000/timer/
        return redirect('/timer/')
    else:
        # return HttpResponse('账户或密码不对')
        return redirect('/login/')

# 登录的页面,二合一操作。
def login(request):
    if request.method == 'GET' :
        return render(request,'login.html')
    else:
        user = request.POST.get('user')
        password = request.POST.get('password')
        print('user:{0} password:{1}'.format(user, password))
        if user == 'lpx' and password == '123':
            return redirect('/timer/')
        else:
            # return HttpResponse('账户或密码不对')
            return redirect('/login/')
