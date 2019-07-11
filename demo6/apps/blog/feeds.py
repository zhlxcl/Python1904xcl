from django.contrib.syndication.views import Feed
from .models import Article
from django.shortcuts import reverse
class ArticleFeed(Feed):
    title = "xcl的博客"
    description = "计算机知识"
    link = "/"

    def items(self):
        return Article.objects.order_by("-create_time")[:3]

    def item_title(self, item):
        return item.title

    def item_link(self, item):
        return reverse("blog:single",args=(item.id,))

    def item_description(self, item):
        return item.author.username + ":" + item.title

