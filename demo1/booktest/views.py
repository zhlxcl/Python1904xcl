from django.shortcuts import render

# 导入响应模块
from django.http import HttpResponse

# MVT中的核心V视图，作用是：接收请求，处理数据，返回响应
# Create your views here.

# 定义视图函数

def index(request):
    return HttpResponse('首页  <br><a href="/booktest/list/">跳转到列表页</a> <a href="/booktest/detail/">跳转到详情页</a>')

def list(request):
    return HttpResponse('列表页 <a href="/booktest/detail/">跳转到详情页</a> <a href="/booktest/index/">跳转到首页</a>')

def detail(request):
    return HttpResponse('详情页 <a href="/booktest/index/">跳转到首页</a> <a href="/booktest/list/">跳转到列表页</a>')
