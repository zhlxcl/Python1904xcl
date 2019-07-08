from django.shortcuts import render,reverse,redirect

# Create your views here.

# 导入响应模块
from django.http import HttpResponse,HttpResponseRedirect,Http404

# 导入获取模板的模块
from django.template import loader

# 导入模型
from .models import Questions,Choice


def index(request):
    return render(request, "myvote/index.html")

def questionlist(request):
    questions = Questions.objects.all()
    return render(request, "myvote/questionlist.html", {"questions": questions})

def choicelist(request,id):
    try:
        question = Questions.objects.get(pk=id)
    except Questions.DoesNotExist:
        return HttpResponse("id非法")
    except Questions.MultipleObjectsReturned:
        return HttpResponse("id非法")


    if request.method == "GET":

        return render(request, "myvote/choicelist.html", {"question": question})
    elif request.method == "POST":
        cid = request.POST.get("choice")
        choice = Choice.objects.get(pk=cid)
        choice.votesnum += 1
        choice.save()
        # 重定向
        return redirect(reverse("myvote:choiceresult", args=(id,)))

def choiceresult(request,id):
    question = Questions.objects.get(pk=id)
    return render(request, "myvote/choiceresult.html", {"question": question})