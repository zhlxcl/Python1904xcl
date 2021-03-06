from django.db import models

# MVT中的M数据模型
# ORM对象
# Create your models here.

# 创建一个BookInfo的数据模型，用来生成一个书籍信息数据表
class BookInfo(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now=True)

    # 在Django后台管理界面上显示对象的列名
    def __str__(self):
        return self.title

# 模型管理器
class HeroInfoManage(models.Manager):
    def addhero(self,_name,_gender,_herotype,_content,_book):
        hero = HeroInfo()
        hero.name = _name
        hero.gender = _gender
        hero.type = _herotype
        hero.content = _content
        hero.book = _book
        hero.save()


# 创建一个HeroInfo的数据模型，用来生成一个英雄信息数据表
class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    # gender = models.BooleanField(default=True)
    gender = models.CharField(max_length=5,choices=(("man","男"),("woman","女")))
    type = models.CharField(max_length=5,choices=(("good","好人"),("bad","坏人")),default="good")
    content = models.CharField(max_length=100)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    myobjects = HeroInfoManage()

    def __str__(self):
        return self.name


class Ads(models.Model):
    desc = models.CharField(max_length=20)
    img = models.ImageField(upload_to="ads")
