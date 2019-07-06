from django.shortcuts import render,reverse,redirect

# Create your views here.
from django.http import HttpResponse

from django.template import loader

from .models import BookInfo,HeroInfo


def index(request):
    return render(request, "book/index.html")

def list(request):
    # return HttpResponse("书籍列表")
    books = BookInfo.objects.all()
    return render(request,"book/list.html",{"books":books})


def detail(request,id):
    # return HttpResponse("英雄详情")
    book = BookInfo.objects.get(pk=id)
    return render(request,"book/detail.html",{"book":book})

def addbook(request):
    if request.method == "GET":
        return render(request, "book/addbook.html")
    elif request.method == "POST":
        title = request.POST.get("booktitle")
        book = BookInfo()
        book.title = title
        book.save()
        return redirect(reverse("book:list"))

def deletebook(request,id):
    # return HttpResponse("删除书籍成功")
    book = BookInfo.objects.get(pk=id)
    book.delete()
    return redirect(reverse("book:list"))

def addhero(request,id):
    # return HttpResponse("添加英雄成功")
    book = BookInfo.objects.get(pk=id)
    if request.method == "GET":
        return render(request, "book/addhero.html", {"book": book})
    elif request.method == "POST":
        name = request.POST.get("username")
        skill = request.POST.get("skill")
        sex = request.POST.get("sex")
        hero = HeroInfo()
        hero.name = name
        hero.sex = sex
        hero.skill = skill
        hero.book = book
        hero.save()
        return redirect(reverse("book:detail", args=(id,)))

def deletehero(request,id):
    # return HttpResponse("删除成功")
    hero = HeroInfo.objects.get(pk=id)
    bookid = hero.book.id
    hero.delete()
    return redirect(reverse("book:detail",args=(bookid,)))

