from django.shortcuts import render,redirect,reverse

# Create your views here.
from django.views.generic import View
from django.http import HttpResponse
from .models import *
from .forms import ArticleForm

# 实现分页器
from django.core.paginator import Paginator,Page



class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()

        # 分页器的功能
        # paginator = Paginator(articles,2) #一页有两篇文章
        # print(paginator.page_range) #[1,5]页数范围
        # print(paginator.object_list) #哪几篇文章
        # print(paginator.num_pages) #总共有几页
        # print(paginator.count)  #总共有几篇文章
        #
        # page = paginator.get_page(3) #得到第几页
        # print(page)
        # print(page.object_list)  #这一页有哪几篇文章
        # print(page.paginator is paginator)
        # print(page.number) #当前页码
        # print(page.has_next()) #是否有下一页
        # print(page.next_page_number())  #下一页的页码
        # print(page.has_previous())  #是否有上一页
        # print(page.previous_page_number())  #上一页的页码

        pagenum = request.GET.get("page")
        # 如pagenum为None,则设置它的值为1，否则为pagenum
        pagenum = 1 if not pagenum else pagenum
        page = Paginator(articles,2).get_page(pagenum)

        return render(request,"blog/index.html",{"page":page,"ads":ads})

class SingleView(View):
    def get(self, request,id):
        article = Article.objects.all()
        return render(request,"blog/single.html")

    def post(self,request,id):
        return render(request,"blog/single.html")


class AddArticleView(View):
    def get(self,request):
        af = ArticleForm()
        return render(request, "blog/addarticle.html",locals())
    def post(self,request):
        af = ArticleForm(request.POST)
        if af.is_valid():
            article = af.save(commit=False)
            article.category = Category.objects.first()
            article.author = User.objects.first()
            article.save()
            return redirect(reverse('blog:index'))

        return HttpResponse("添加成功")










