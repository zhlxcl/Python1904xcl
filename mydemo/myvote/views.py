from django.shortcuts import render,reverse,redirect,get_object_or_404

# Create your views here.

# 导入响应模块
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse

# 导入获取模板的模块
from django.template import loader

# 导入模型
from .models import Questions,Choice,VoteUser

# 导入注册，登录，激活
from django.contrib.auth import login as lgi ,logout as lgo ,authenticate

# 导入表单类
from .forms import *

# 验证码的生成
from PIL import Image,ImageDraw,ImageFont
import random,io
from django.core.cache import cache

#邮箱验证
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings
# from itsdangerous import TimedJSONWebSignatureSerializer
# from django.conf import settings



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
# def checklogin(fun):
#     def check(request,*args):
#         username = request.session.get("username")
#         if username:
#             return fun(request,*args)
#         else:
#             return redirect(reverse("myvote:login"))
#     return check

# 3.使用django自带的授权方式的装饰器
def checklogin(fun):
    def check(request,*args):
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return redirect(reverse("myvote:login"))
    return check



# 首页---问题列表页
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
    # username = request.session.get("username")
    # questions = Questions.objects.all()
    # return render(request, "myvote/login.html",locals())

    # 3.使用Django授权模式
    # print(request.user)    #没有用户登录 request.user为AnonymousUser匿名用户
    # if request.user:
    #     print(request.user.is_authenticated)
    questions = Questions.objects.all()
    return render(request,"myvote/index.html",locals())

#选项列表页
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

# 结果展示页
@checklogin
def choiceresult(request, id):
    # return HttpResponse("选项页")
    # question = Questions.objects.get(pk=id)
    question = get_object_or_404(Questions, pk=id)
    return render(request, "myvote/choiceresult.html", locals())



#一.使用cookie，session
# def login(request):
#     if request.method == "GET":
#         return render(request, "myvote/login.html")
#     elif request.method == "POST":
#         # 检测用户名密码是否对应
#         # 1.登录成功需要存储cookie（cookie是在response中设置的）
#         # response = redirect(reverse("myvote:index"))
#         # # 存储cookie值
#         # response.set_cookie("username",request.POST.get("username"))
#         # return response
#         # 2.使用session存储数据（session是在request中设置的）
#         request.session["username"] = request.POST.get("username")
#         return redirect(reverse("myvote:index"))
# def logout(request):
#     # 1.删除cookie值
#     # res = redirect(reverse("myvote:login"))
#     # res.delete_cookie("username")
#     # return res
#     # 2.删除session值
#     request.session.flush()
#     return redirect(reverse("myvote:login"))


# 二.使用django自带的授权方式，实现注册，登录，退出
# # 登录
# def login(request):
#     if request.method == "GET":
#         return render(request,'myvote/login.html')
#     elif request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         user = authenticate(request,username = username,password=password)
#         if user:
#             lgi(request,user)
#             return redirect(reverse("myvote:index"),args=(user,))
#         else:
#             return render(request, 'myvote/login.html', {"errors": "登录失败"})
# # 退出
# def logout(request):
#     lgo(request)
#     return redirect(reverse("myvote:login"))
# #注册
# def regist(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         try:
#             user = VoteUser.objects.create_user(username=username, password=password)
#         except:
#             user = None
#         if user:
#             return redirect(reverse("myvote:login"))
#         else:
#             return render(request, 'myvote/login.html', {"errors":"注册失败"})


#********由Django的表单类生成表单************
# 登录
def login(request):
    # 获取表单类
    lgf = LoginForm()
    rgf = RegistForm()
    if request.method == "GET":

        # 发送邮件验证
        recvlist = ["18614986528@163.com","2870175885@qq.com"]

        try:
            send_mail("邮箱发送验证","这是一封邮件",settings.EMAIL_HOST_USER,recvlist)
            print("send success")
        except Exception as e:
            print(e)

        return render(request,'myvote/login.html',{"lgf":lgf,"rgf":rgf})
    elif request.method == "POST":
        # 验证码的判断
        verifycode = request.POST.get("verify")
        if not verifycode == cache.get("verify"):
            return HttpResponse("验证码错误")

        lgf = LoginForm(request.POST)
        if lgf.is_valid():
            username = lgf.cleaned_data["username"]
            password = lgf.cleaned_data["password"]
            user = authenticate(request,username = username,password=password)
            if user:
                lgi(request,user)
                return redirect(reverse("myvote:index"))
            else:
                return render(request, 'myvote/login.html', {"errors": "登录失败","lgf":lgf,"rgf":rgf})
        else:
            return render(request, 'myvote/login.html', {"errors": "登录失败","lgf":lgf,"rgf":rgf})
# 退出
def logout(request):
    lgo(request)
    return redirect(reverse("myvote:login"))
# 注册
def regist(request):
    if request.method == "POST":
        rgf = RegistForm(request.POST)
        if rgf.is_valid():
            # 先返回一个user 此时没有保存数据库应为密码还没有加密
            user = rgf.save(commit=False)
            # 对user用户设置密码 加密过得密码
            user.set_password(rgf.cleaned_data["password"])
            # 保存数据库
            user.save()
            return redirect(reverse("myvote:login"))
        else:
            lgf = LoginForm()
            rgf = RegistForm()
            return render(request, 'myvote/login.html', {"errors": "注册失败","lgf":lgf,"rgf":rgf})
    else:
        return HttpResponse("错误")


# **************用户输入框验证****************
def checkuser(request):
    if request.method == "GET":
        name = request.GET.get("name")
        qs = VoteUser.objects.filter(username=name)
        print(qs)
        user = qs.first()
        print(user)
        if user:
            return JsonResponse({"state":1})
        else:
            return JsonResponse({"state":0,'errorinfo':"用户名不存在"})






# *******************************************************

# 用来生成验证码
def verify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 100
    heigth = 25
    # 创建画面对象
    im = Image.new('RGB', (width, heigth), bgcolor)
    # 创建画笔对象
    draw = ImageDraw.Draw(im)
    # 调用画笔的point()函数绘制噪点
    for i in range(0, 100):
        xy = (random.randrange(0, width), random.randrange(0, heigth))
        fill = (random.randrange(0, 255), 255, random.randrange(0, 255))
        draw.point(xy, fill=fill)
    # 定义验证码的备选值
    str1 = 'ABCD123EFGHIJK456LMNOPQRS789TUVWXYZ0'
    # 随机选取4个值作为验证码
    rand_str = ''
    for i in range(0, 4):
        rand_str += str1[random.randrange(0, len(str1))]
    cache.set("verify", rand_str)
    # 构造字体对象
    font = ImageFont.truetype('CALISTBI.TTF', 23)
    fontcolor = (255, random.randrange(0, 255), random.randrange(0, 255))
    # 绘制4个字
    draw.text((5, 2), rand_str[0], font=font, fill=fontcolor)
    draw.text((25, 2), rand_str[1], font=font, fill=fontcolor)
    draw.text((50, 2), rand_str[2], font=font, fill=fontcolor)
    draw.text((75, 2), rand_str[3], font=font, fill=fontcolor)
    # 释放画笔
    del draw
    # request.session['verifycode'] = rand_str
    f = io.BytesIO()
    im.save(f, 'png')
    # 将内存中的图片数据返回给客户端，MIME类型为图片png
    return HttpResponse(f.getvalue(), 'image/png')