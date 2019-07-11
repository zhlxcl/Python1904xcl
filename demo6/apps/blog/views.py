from django.shortcuts import render,redirect,reverse,get_object_or_404
from django.http import HttpResponse
from django.views.generic import View
from .models import *
# Create your views here.

from .forms import ArticleForm,CommentForm

# 实现分页器
from django.core.paginator import Paginator,Page


# 封装一个实现文章分页的方法
def getpage(request,object_list,per_num):
    pagenum = request.GET.get("page")
    # 如pagenum为None,则设置它的值为1，否则为pagenum
    pagenum = 1 if not pagenum else pagenum
    page = Paginator(object_list, per_num).get_page(pagenum)
    return page




class IndexView(View):
    def get(self,request):
        ads = Ads.objects.all()
        articles = Article.objects.all()
        # pagenum = request.GET.get("page")
        # # 如pagenum为None,则设置它的值为1，否则为pagenum
        # pagenum = 1 if not pagenum else pagenum
        # page = Paginator(articles, 2).get_page(pagenum)

        page = getpage(request,articles,2)

        return render(request, "blog/index.html", {"page": page, "ads": ads})

class SingleView(View):
    def get(self,request,id):
        article = get_object_or_404(Article,pk=id)
        article.views += 1
        article.save()
        cf = CommentForm()
        return render(request,"blog/single.html",{"article":article,"cf":cf})
    def post(self,request,id):
        article = get_object_or_404(Article, pk=id)
        cf = CommentForm(request.POST)
        comment = cf.save(commit=False)
        comment.article = article
        comment.save()
        return redirect(reverse("blog:single",args=(article.id,)))


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


class ArchivesView(View):
    def get(self,request,year,month):
        articles = Article.objects.filter(create_time__year = year,create_time__month = month)
        ads = Ads.objects.all()
        page = getpage(request,articles,1)

        return render(request,"blog/index.html",{"page":page, "ads": ads})

class CategorysView(View):
    def get(self,request,id):
        category = get_object_or_404(Category,pk=id)
        articles = category.article_set.all()
        ads = Ads.objects.all()
        page = getpage(request,articles,1)
        return render(request,'blog/index.html',{"page":page, "ads": ads})

class TagsView(View):
    def get(self,request,id):
        tag = get_object_or_404(Tag,pk=id)
        articles = tag.article_set.all()
        ads = Ads.objects.all()
        page = getpage(request,articles,1)
        return render(request, 'blog/index.html', {"page": page, "ads": ads})
