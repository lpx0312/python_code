from django.shortcuts import render
import  datetime

# Create your views here.




def index(request):

    s = 'hello world'
    l = ['西游记','红楼梦','水浒传','三国演义']
    books = []
    dic = {'name':'yuan','age':28}
    file_size = 12346546
    story = "hello world sdklfjaljsflmslmfdlm"
    link =  "<a href=''>baidu</a>"
    score=request.GET.get('score')
    score = int(score) if score else None
    print('score=',score)
    print(type(score))
    ### 变量渲染 {{  }}

    now = datetime.datetime.now()

    ### 标签渲染 {% tag_name %}

    return  render(request,'index.html',{'s':s,'l':l,'dic':dic,'now':now,'books':books,'file_size':file_size,'story':story,'link':link,'score':score})


def books(request):
    return render(request,'books.html')

def orders(request):
    return render(request,'orders.html')