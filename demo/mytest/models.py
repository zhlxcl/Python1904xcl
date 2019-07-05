from django.db import models

# Create your models here.
class MyBook(models.Model):
    title = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class MyHero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField(default=True)
    content = models.CharField(max_length=100)
    book = models.ForeignKey(MyBook,on_delete=models.CASCADE)
    def __str__(self):
        return self.name



# 数据库关系

# 一对一
class Account(models.Model):
    name = models.CharField(max_length=20)

class Inform(models.Model):
    phone = models.CharField(max_length=11)
    account = models.OneToOneField(Account,on_delete=models.CASCADE)

# 多对多
class Host(models.Model):
    hostname = models.CharField(max_length=32)

class Application(models.Model):
    name = models.CharField(max_length=32)
    h = models.ManyToManyField(to='Host')
