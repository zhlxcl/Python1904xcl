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

# 收货人信息
class ConsigneeView(View):
    def get(self,request):
        return render(request,"gift/consignee.html")

# 订单支付成功
class OrderSuccessView(View):
    def get(self,request):
        return render(request,"gift/ordersuccess.html")

# 创建订单
def createmyorder(request):
    mycart = Cart.objects.filter(user=request.user)
    sum = 0
    # print(len(mycart))
    if len(mycart) == 0:
        sum = str("空空如也，无法结算")
        return JsonResponse({"sum":sum })
    else:
        for i in mycart:
            price = i.good.price
            num = i.num
            sum += price * num
            g = Good.objects.get(pk=i.good.id)
            newstock = g.stock - num
            newsale = g.sale + num
            g.stock = newstock
            g.sale = newsale
            g.save()

        order = Order()
        order.sum = sum
        order.user = request.user
        order.save()
        for i in mycart:
            ordergoods = OrderGoods()
            ordergoods.order = order
            ordergoods.good = i.good
            ordergoods.save()
            i.delete()
        return JsonResponse({"sum": sum})


def product(request):
    return render(request, "gift/product.html")



# 判断用户是否登录的装饰器
def checklogin(fun):
    def check(request,*args):
        if request.user and request.user.is_authenticated:
            return fun(request,*args)
        else:
            return redirect(reverse("gift:login"))
    return check

# 加入购物车
@checklogin
def addcart(request):
    goodnum = int(request.POST.get("goodnum"))
    goodid = request.POST.get("goodid")
    good = Good.objects.get(pk=goodid)
    usercart = Cart.objects.filter(user=request.user,good=good).first()
    if usercart:
        usercart.num += goodnum
        usercart.save()
    else:
        cart = Cart()
        cart.user = request.user
        cart.good = good
        cart.num = goodnum
        cart.save()
    return redirect(reverse("gift:cart"))

# 删除购物车中的商品
def delcart(request,id):
    cart = Cart.objects.get(pk=id)
    cart.delete()
    return redirect(reverse("gift:cart"))

# 清空购物车
def clearcart(request):
    mycart = Cart.objects.filter(user=request.user)
    for i in mycart:
        i.delete()
    return JsonResponse({"sum": "更新成功"})
# 购物车信息详情
class CartView(View):
    def get(self,request):
        mycart = Cart.objects.filter(user=request.user)
        # print(mycart)
        return render(request,"gift/cart.html",locals())

# 修改购物车中的商品的数量
def changenum(request,id):
    cnum = int(request.POST.get("num"))
    cart = Cart.objects.get(pk=id)
    stock = cart.good.stock
    price = cart.good.price
    if cnum > stock:
        cart.num = stock
        cart.save()
        sumprice = price * stock
        return JsonResponse({"num": stock,"sumprice": sumprice})
    else:
        cart.num = cnum
        cart.save()
        sumprice = price * cnum
        return JsonResponse({"num": cnum, "sumprice": sumprice})

# 得到不同种类的商品
def diffcategory(request,id):
    category = Category.objects.get(pk=id)
    goods = category.good_set.all()[:6]
    goodlist = []
    for i in goods:
        good = {
            'id': i.id,
            'goodname': i.goodname,
            'price': i.price,
            'maximg': str(i.maximg),
            'sale':i.sale,
        }
        goodlist.append(good)
    return JsonResponse(goodlist, safe=False)
# 六种商品
def allgoods(request):
    goods = Good.objects.all()[:6]
    goodlist = []
    for i in goods:
        good = {
            'id': i.id,
            'goodname': i.goodname,
            'price': i.price,
            'maximg': str(i.maximg),
            'sale':i.sale,
        }
        goodlist.append(good)
    return JsonResponse(goodlist, safe=False)

# 所有商品
def all(request):
    goods = Good.objects.all()
    goodlist = []
    for i in goods:
        good = {
            'id': i.id,
            'goodname': i.goodname,
            'price': i.price,
            'maximg': str(i.maximg),
            'sale':i.sale,
        }
        goodlist.append(good)
    return JsonResponse(goodlist, safe=False)



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

# 所有订单信息
def myorder(request):
    orderlist = Order.objects.filter(user=request.user)
    return render(request,"gift/myorder.html",locals())

# 查看订单详情
def showorderdetail(request,id):
    order = Order.objects.get(pk=id)
    ordergood = order.ordergoods_set.all()
    # print(ordergood)
    goodlist = []
    for i in ordergood:
        good = {
            'goodname':i.good.goodname,
            'id':i.good.id,
            'price':i.good.price,
        }
        goodlist.append(good)
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









