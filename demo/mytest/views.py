from django.shortcuts import render
# 导入响应模块
from django.http import HttpResponse
# 导入获取模板的模块
from django.template import loader
# 导入模型
from .models import MyBook,MyHero
# 定义视图函数
def index(request):
    temp1 = loader.get_template("mytest/index.html")
    result = temp1.render({"name":"xcl"})
    return HttpResponse(result)
def list(request):
    temp2 = loader.get_template("mytest/list.html")
    books = MyBook.objects.all()
    result = temp2.render({"books":books})
    return HttpResponse(result)
def detail(request,id):
    temp3 = loader.get_template("mytest/detail.html")
    book = MyBook.objects.get(pk=id)
    result = temp3.render({"book":book})
    return HttpResponse(result)
