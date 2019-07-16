from django.db import models
from django.contrib.auth.models import User
# Create your models here.


# 会员用户信息表
class Member(User):
    # 会员手机号
    telephone = models.CharField(max_length=11)
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
    # 商品类型
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    # 商品标签
    tags = models.ManyToManyField(Tag)
    # 商品颜色
    colors = models.ManyToManyField(Color)
    def __str__(self):
        return self.goodname
