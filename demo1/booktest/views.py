from django.shortcuts import render

# 导入响应模块
from django.http import HttpResponse

# 导入获取模板的模块
from django.template import loader

# 导入模型
from .models import BookInfo,HeroInfo

# MVT中的核心V视图，作用是：接收请求，处理数据，返回响应
# Create your views here.

# 定义视图函数

def index(request):
    # return HttpResponse('首页  <br><a href="/booktest/list/">跳转到列表页</a>')

    # #1.获取模板(写入页面的位置)
    # temp1 = loader.get_template("booktest/index.html")
    # # 2.使用模板渲染字典参数
    # result = temp1.render({"name":"xcl"})
    # # 3.将渲染的结果返回
    # return HttpResponse(result)

    return render(request,"booktest/index.html",{"name":"xcl"})

def list(request):
    # s = '''
    #     <br>
    #     <a href="/booktest/detail/1/">跳转到详情页1</a><br>
    #     <a href="/booktest/detail/2/">跳转到详情页2</a><br>
    #     <a href="/booktest/detail/2/">跳转到详情页3</a><br>
    # '''
    # return HttpResponse('列表页%s'%(s,))

    # temp2 = loader.get_template("booktest/list.html")
    #
    # books = BookInfo.objects.all()
    # result = temp2.render({"books":books})
    # return HttpResponse(result)

    books = BookInfo.objects.all()
    return render(request,"booktest/list.html",{"books":books})

def detail(request,id):
    # return HttpResponse('这是%s详情页 <a href="/booktest/">跳转到首页</a>'%(id,))

    # temp3 = loader.get_template("booktest/detail.html")
    #
    # book = BookInfo.objects.get(pk=id)
    # result = temp3.render({"book":book})
    # return HttpResponse(result)

    book = BookInfo.objects.get(pk=id)
    return render(request,"booktest/detail.html",{"book":book})