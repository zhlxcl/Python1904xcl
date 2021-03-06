
from django.template import library
register = library.Library()

from gift.models import Good,Category

# 得到销量最高的四种商品
@register.simple_tag
def gethighsalegoods(num=4):
    return Good.objects.order_by("-sale")[:num]

# 得到类型为 礼物 的商品
@register.simple_tag
def getallgoods(num=4):
    return Good.objects.all()[:num]

# 得到类型为 鲜花 的销量前六的商品
@register.simple_tag
def getflowergoods(num=6):
    cate = Category.objects.filter(title="鲜花").first()
    goods = Good.objects.filter(category=cate.id).order_by("-sale")[:num]
    # print(goods)
    return goods

# 得到类型为 蛋糕 的销量前五的商品
@register.simple_tag
def getheighcakegoods(num=5):
    cate = Category.objects.filter(title="蛋糕").first()
    goods = Good.objects.filter(category=cate.id).order_by("-sale")[:num]
    # print(goods)
    return goods

# 得到销量最高的1种商品
@register.simple_tag
def getonegoods(num=1):
    return Good.objects.order_by("-sale")[:num]

# 得到五个分类的类名
@register.simple_tag
def getallcategory(num=5):
    return Category.objects.order_by("id")[:num]
