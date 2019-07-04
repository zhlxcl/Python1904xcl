from django.db import models

# Create your models here.

class Questions(models.Model):
    # 问题标题
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

class Choice(models.Model):
    # 选项标题
    title = models.CharField(max_length=30)
    # 选项所属的问题
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    # 选项被选择的次数
    votesnum = models.IntegerField(default=0)

    def __str__(self):
        return self.title