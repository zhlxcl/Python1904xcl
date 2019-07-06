from django.shortcuts import render,redirect,reverse

# Create your views here.
from django.http import HttpResponse
from .models import Question,Choice

def index(request):
    # return HttpResponse("首页")
    questions = Question.objects.all()
    return render(request,"polls/index.html",{"questions":questions})


def choicelist(request,id):
    # return HttpResponse("结果页")
    question = Question.objects.get(pk=id)
    if request.method == 'GET':
        return render(request,"polls/choicelist.html",{"question":question})
    elif request.method == 'POST':
        cid = request.POST.get("choice")
        choice = Choice.objects.get(pk=cid)
        choice.votenum += 1
        choice.save()
        return redirect(reverse("polls:result",args=(id,)))

def result(request, id):
    # return HttpResponse("选项页")
    question = Question.objects.get(pk=id)
    return render(request, "polls/result.html", {"question": question})
