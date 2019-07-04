from django.shortcuts import render,reverse,redirect

# Create your views here.

# 导入响应模块
from django.http import HttpResponse,HttpResponseRedirect

# 导入获取模板的模块
from django.template import loader

# 导入模型
from .models import Questions,Choice


def index(request):
    questions = Questions.objects.all()
    return render(request, "myvote/index.html",{"questions":questions})

def questionlist(request):
    questions = Questions.objects.all()
    return render(request, "myvote/questionlist.html", {"questions": questions})

def choicelist(request,id):
    if request.method == "GET":
        questions = Questions.objects.get(pk=id)
        return render(request, "myvote/choicelist.html", {"questions": questions})
    elif request.method == "POST":
        cid = request.POST.get("choice")
        choice = Choice.objects.get(pk=cid)
        choice.votesnum += 1
        choice.save()
        return redirect(reverse("myvote:choiceresult", args=(id,)))

def choiceresult(request,id):
    questions = Questions.objects.get(pk=id)
    return render(request, "myvote/choiceresult.html", {"questions": questions})