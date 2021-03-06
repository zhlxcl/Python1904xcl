from django.db import models

# Create your models here.

class BookInfo(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class HeroInfo(models.Model):
    name = models.CharField(max_length=20)
    sex = models.CharField(max_length=5,choices=(("man","男"),("woman","女")))
    skill = models.CharField(max_length=20)
    book = models.ForeignKey(BookInfo,on_delete=models.CASCADE)

    def __str__(self):
        return self.name

