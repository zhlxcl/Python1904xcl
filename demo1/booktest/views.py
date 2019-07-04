from django.shortcuts import render,reverse,redirect

# 导入响应模块
from django.http import HttpResponse,HttpResponseRedirect

# 导入获取模板的模块
from django.template import loader

# 导入模型
from .models import BookInfo,HeroInfo

# MVT中的核心V视图，作用是：接收请求，处理数据，返回响应
# Create your views here.

# 基于类的视图操作(调用底层类)
from django.views.generic import View,TemplateView,ListView

class IndexView(View):
    def get(self,request):
        # 重写get方法，来完成get请求的返回
        return render(request,"booktest/index.html",{"name":"xcl"})

class IndexTemplateView(TemplateView):
    template_name = "booktest/index.html"
    def get_context_data(self):
        return {"name":"xcl"}

class ListView(ListView):
    # 指定模型
    model = BookInfo
    # 指定模板页面
    template_name = "booktest/list.html"
    # 指定页面参数
    context_object_name = "books"

    # 定义函数设置页面显示数据的个数，显示前3个
    def get_queryset(self):
        return BookInfo.objects.all()


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

def deletebook(request,id):
    # return HttpResponse("删除书籍成功")
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse("booktest:list"))

def addbook(request):
    if request.method == "GET":
        return render(request, "booktest/addbook.html")
    elif request.method == "POST":
        title = request.POST.get("booktitle")
        book = BookInfo()
        book.title = title
        book.save()
        return redirect(reverse("booktest:list"))

def addhero(request,id):
    # return HttpResponse("添加英雄成功")
    book = BookInfo.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "booktest/addhero.html", {"book": book})
    elif request.method == "POST":
        name = request.POST.get("username")
        content = request.POST.get("content")
        gender = request.POST.get("gender")
        type = request.POST.get("type")
        hero = HeroInfo()
        hero.name = name
        hero.gender = gender
        hero.type = type
        hero.content = content
        hero.book = book
        hero.save()
        return redirect(reverse("booktest:detail", args=(id,)))

def deletehero(request,id):
    # return HttpResponse("删除成功")

    hero = HeroInfo.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()

    # 1.重定向
    # return HttpResponseRedirect("/detail/" + str(bookid) + "/" )
    #2.
    # result = reverse("booktest:detail",args=(bookid,))
    # return redirect("/detail/" + str(bookid) + "/" )
    # 3.
    return redirect(reverse("booktest:detail",args=(bookid,)))