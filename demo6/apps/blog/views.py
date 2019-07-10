from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse
from django.views.generic import View
from .models import *
# Create your views here.

from .forms import ArticleForm

# 实现分页器
from django.core.paginator import Paginator,Page

class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        pagenum = request.GET.get("page")
        # 如pagenum为None,则设置它的值为1，否则为pagenum
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(articles, 2).get_page(pagenum)

        return render(request, "blog/index.html", {"page": page, "ads": ads})

class SingleView(View):
    def get(self,request,id):
        return render(request,"blog/single.html")

class AddArticleView(View):
    def get(self,request):
        af = ArticleForm()
        return render(request,"blog/addarticle.html",locals())
    def post(self,request):
        af = ArticleForm(request.POST)
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))

        return HttpResponse("添加成功")
