from django.conf.urls import url
from . import views

from .feeds import ArticleFeed

app_name = 'blog'

urlpatterns = [
    url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^single/(\d+)/$',views.SingleView.as_view(),name="single"),
    url(r'^addarticle/$',views.AddArticleView.as_view(),name="addarticle"),
    url(r'^archives/(\d+)/(\d+)/$',views.ArchivesView.as_view(),name='archives'),
    url(r'^categorys/(\d+)/$',views.CategorysView.as_view(),name='categorys'),
    url(r'^tags/(\d+)/$',views.TagsView.as_view(),name='tags'),
    url(r'^rss/$',ArticleFeed(),name='rss'),
]