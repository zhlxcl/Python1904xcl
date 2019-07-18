from django.conf.urls import url
from . import views

app_name = 'gift'

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name="index"),
    url(r'^login/$', views.LoginView.as_view(), name="login"),
    url(r'^logout/(\d+)/$', views.logout, name="logout"),
    url(r'^verify/$', views.verify, name="verify"),
    url(r'^regist/$', views.RegistView.as_view(), name="regist"),
    url(r'^cart/$', views.CartView.as_view(), name="cart"),
    url(r'^detail/(\d+)/$', views.DetailView.as_view(), name="detail"),
    url(r'^recommend/(\d+)/$', views.recommend, name="recommend"),
    url(r'^customer/$', views.CustomerView.as_view(), name="customer"),

    # 低价商品
    url(r'^lowerprice/$', views.lowerprice, name="lowerprice"),
    # 推荐商品
    url(r'^progoods/$', views.progoods, name="progoods"),
    # 新品推荐
    url(r'^newgoods/$', views.newgoods, name="newgoods"),
    # 猜你喜欢
    url(r'^youlovegoods/$', views.youlovegoods, name="youlovegoods"),

    # 添加购物车
    url(r'^addcart/(\d+)/$', views.addcart, name="addcart"),

]