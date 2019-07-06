from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=30)

    def __str__(self):
        return self.title

class Choice(models.Model):
    title = models.CharField(max_length=30)
    votenum = models.IntegerField(max_length=10,default=0)
    question = models.ForeignKey(Question,on_delete=models.CASCADE)

    def __str__(self):
        return self.title