from django.shortcuts import render,reverse,redirect

# Create your views here.

from django.http import HttpResponse,JsonResponse

from django.views.generic import View

# 导入模型
from .models import *
# 导入注册，登录，激活
from django.contrib.auth import login,logout as lgo,authenticate

# 验证码的生成
from PIL import Image,ImageDraw,ImageFont
import random,io
from django.core.cache import cache



# 首页
class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        return render(request,"gift/index.html",{"ads":ads})

# 低价商品
def lowerprice(request):
    goods = Good.objects.order_by("price")[:4]
    goodlist = []
    for i in goods:
        good = {
            'id': i.id,
            'goodname': i.goodname,
            'price': i.price,
            'maximg': str(i.maximg),
        }
        goodlist.append(good)
    return JsonResponse(goodlist, safe=False)

# 商城推荐库存最多的商品
def progoods(request):
    goods = Good.objects.order_by("-stock")[:4]
    goodlist = []
    for i in goods:
        good = {
            'id': i.id,
            'goodname': i.goodname,
            'price': i.price,
            'maximg': str(i.maximg),
        }
        goodlist.append(good)
    return JsonResponse(goodlist, safe=False)

# 新品推荐(id最大的)
def newgoods(request):
    goods = Good.objects.order_by("-id")[:4]
    goodlist = []
    for i in goods:
        good = {
            'id': i.id,
            'goodname': i.goodname,
            'price': i.price,
            'maximg': str(i.maximg),
        }
        goodlist.append(good)
    return JsonResponse(goodlist, safe=False)

# 猜你喜欢(销售最高的)
def youlovegoods(request):
    goods = Good.objects.order_by("-sale")[:4]
    goodlist = []
    for i in goods:
        good = {
            'id': i.id,
            'goodname': i.goodname,
            'price': i.price,
            'maximg': str(i.maximg),
        }
        goodlist.append(good)
    return JsonResponse(goodlist, safe=False)


# 用户登录
class LoginView(View):
    def get(self,request):
        return render(request,"gift/login.html")
    def post(self,request):
        # 验证码的判断
        verifycode = request.POST.get("verify")
        if not verifycode == cache.get("verify"):
            return HttpResponse("验证码错误")
        # return render(request, "gift/index.html")

        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request,username = username,password=password)

        if user:
            user.member.status = 1
            user.member.save()
            login(request,user)
            return redirect(reverse("gift:index"),args=(user,))
        else:
            return render(request, 'gift/login.html', {"errors": "登录失败,信息有误"})

# 用户退出
def logout(request,id):
    user = User.objects.get(pk=id)
    user.member.status = 0
    user.member.save()
    lgo(request)
    return redirect(reverse("gift:index"))

# 用户注册
class RegistView(View):
    def get(self,request):
        return render(request,"gift/login.html")
    def post(self,request):
        username = request.POST.get("username")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        email = request.POST.get("email")
        if password1 == password2:
            try:
                user = Member.objects.create_user(username=username, password=password1, email=email)
            except:
                user = None
            if user:
                return redirect(reverse("gift:login"))
            else:
                return render(request, 'gift/login.html', {"errors": "用户已存在，注册失败"})
        else:
            return render(request, 'gift/login.html', {"errors": "两次密码输入不一致，注册失败"})


# 加入购物车
def addcart(request,id):

    num = request.POST.get("goodnum")
    mycart = Cart()
    return JsonResponse({"n":n})

# 购物车
class CartView(View):
    def get(self,request):
        return render(request,"gift/cart.html")

# 商品详情
class DetailView(View):
    def get(self,request,id):
        good = Good.objects.get(pk=id)
        # cate = good.category
        # print(cate.title,type(cate.title))
        return render(request,"gift/detail.html",{"good":good})

# 同类型商品推荐
def recommend(request,id):
    good = Good.objects.get(pk=id)
    name = good.goodname
    cate = good.category
    goods = Good.objects.filter(category=cate.id).order_by("-sale")[:5]
    # print(goods,type(goods))
    goodlist = []
    for i in goods:
        if i.goodname != name:
            g = {
                'id':i.id,
                'goodname':i.goodname,
                'price':i.price,
                'sale':i.sale,
                'maximg': str(i.maximg),
            }
            goodlist.append(g)
    return JsonResponse(goodlist,safe=False)


# 用户收货信息
class CustomerView(View):
    def get(self, request):
        return render(request, "gift/customer.html")

# 用来生成验证码
def verify(request):
    # 定义变量，用于画面的背景色、宽、高
    bgcolor = (random.randrange(20, 100),
               random.randrange(20, 100),
               random.randrange(20, 100))
    width = 110
    heigth = 28
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









