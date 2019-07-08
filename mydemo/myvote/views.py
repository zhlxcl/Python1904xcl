from django.shortcuts import render,reverse,redirect,get_object_or_404

# Create your views here.

# 导入响应模块
from django.http import HttpResponse,HttpResponseRedirect,Http404

# 导入获取模板的模块
from django.template import loader

# 导入模型
from .models import Questions,Choice


# 装饰器
# 1.使用cookie的装饰器
# def checklogin(fun):
#     def check(request,*args):
#         username = request.COOKIES.get("username")
#         if username:
#             return fun(request,*args)
#         else:
#             return redirect(reverse("myvote:login"))
#     return check

#2.使用session的装饰器
def checklogin(fun):
    def check(request,*args):
        username = request.session.get("username")
        if username:
            return fun(request,*args)
        else:
            return redirect(reverse("myvote:login"))
    return check


def login(request):

    if request.method == "GET":
        return render(request, "myvote/login.html")
    elif request.method == "POST":
        # 检测用户名密码是否对应
        # 1.登录成功需要存储cookie（cookie是在response中设置的）
        # response = redirect(reverse("myvote:index"))
        # # 存储cookie值
        # response.set_cookie("username",request.POST.get("username"))
        # return response
        # 2.使用session存储数据（session是在request中设置的）
        request.session["username"] = request.POST.get("username")
        return redirect(reverse("myvote:index"))

def logout(request):
    # 1.删除cookie值
    # res = redirect(reverse("myvote:login"))
    # res.delete_cookie("username")
    # return res
    # 2.删除session值
    request.session.flush()
    return redirect(reverse("myvote:login"))



@checklogin
def index(request):
    # 未使用装饰器的判断
    # username = request.COOKIES.get("username")
    # if username:
    #     questions = Questions.objects.all()
    #     return render(request, "myvote/index.html",locals())
    # else:
    #     return redirect(reverse("myvote:login"))

    # 1.使用cookie获取值
    # username = request.COOKIES.get("username")
    # 2.使用session获取值
    username = request.session.get("username")

    questions = Questions.objects.all()
    return render(request, "myvote/index.html",locals())


@checklogin
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

@checklogin
def choiceresult(request, id):
    # return HttpResponse("选项页")
    question = Questions.objects.get(pk=id)
    get_object_or_404(Question, pk=id)
    return render(request, "myvote/choiceresult.html", locals())