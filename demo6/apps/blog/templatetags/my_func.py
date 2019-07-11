# 自定义模板表达式，扩展Django原有功能

from django.template import library
register = library.Library()

from blog.models import Article,Category,Tag

@register.simple_tag
def getlatestarticles(num=3):
    return Article.objects.order_by("-create_time")[:num]


@register.simple_tag
def getcategoryarticles(num=3):
    return Category.objects.all()

@register.simple_tag
def getalltags(num=3):
    return Tag.objects.all()

@register.simple_tag
def gettimes(num=3):
    return Article.objects.dates("create_time","month","DESC")