from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 会员用户信息表
class Member(User):
    # 会员手机号
    telephone = models.CharField(max_length=11)
    # 会员登录状态
    status = models.IntegerField(default=0)
    def __str__(self):
        return self.username

# 购物收货人信息表
class Customer(models.Model):
    # 收货人姓名
    name = models.CharField(max_length=20)
    # 收货人地址
    address = models.CharField(max_length=50)
    # 收货人电话
    telephone = models.CharField(max_length=11)
    # 收货人邮箱
    email = models.EmailField()
    # 会员用户账号
    member = models.ForeignKey(Member,on_delete=models.CASCADE)



# 商品颜色列表
class Color(models.Model):
    title = models.CharField(max_length=10)
    def __str__(self):
        return self.title

# 商品类型列表
class Category(models.Model):
    title = models.CharField(max_length=20)
    def __str__(self):
        return self.title

# 商品标签列表
class Tag(models.Model):
    title = models.CharField(max_length=15)
    def __str__(self):
        return self.title

# 商品信息表
class Good(models.Model):
    # 商品名
    goodname = models.CharField(max_length=10)
    # 商品价格
    price = models.IntegerField()
    # 商品库存量
    stock = models.IntegerField(default=0)
    # 商品销量
    sale = models.IntegerField()
    # 商品简介
    detail = models.CharField(max_length=200)
    # 商品小图片
    img = models.ImageField(upload_to="gds")
    # 商品大图片
    maximg = models.ImageField(upload_to="gds")
    # 商品类型
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 商品标签
    tags = models.ManyToManyField(Tag)
    # 商品颜色
    color = models.ManyToManyField(Color)
    def __str__(self):
        return self.goodname

# 轮播广告图
class Ads(models.Model):
    img = models.ImageField(upload_to="ads")
    desc = models.CharField(max_length=20)
    index = models.IntegerField(default=0)
    def __str__(self):
        return self.desc

# 用户购物车
class Cart(models.Model):
    # 用户
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    # 商品
    good = models.ForeignKey(Good,on_delete=models.CASCADE)
    # 商品数量
    num = models.IntegerField()

# 用户订单
class Order(models.Model):
    # 用户
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # 订单总价
    sum = models.IntegerField()
    # 订单时间
    create_time = models.DateTimeField(auto_now_add=True)

#  用户订单中的商品
class OrderGoods(models.Model):
    # 订单号
    order = models.ForeignKey(Order,on_delete=models.CASCADE)
    # 商品
    good = models.ForeignKey(Good,on_delete=models.CASCADE)