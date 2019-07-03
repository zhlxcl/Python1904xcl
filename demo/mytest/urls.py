
from django.conf.urls import url
from . import views
# 应用路由配置
urlpatterns = [
    url(r'^$',views.index),
    url(r'^list/$',views.list),
    url(r'^detail/(\d+)/$', views.detail),
]
