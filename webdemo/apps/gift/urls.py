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

    url(r'^product/$', views.product, name="product"),
    url(r'^consignee/$', views.ConsigneeView.as_view(), name="consignee"),
    url(r'^ordersuccess/$', views.OrderSuccessView.as_view(), name="ordersuccess"),
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
    # 添加购物车商品
    url(r'^addcart/$', views.addcart, name="addcart"),
    # 删除购物车商品
    url(r'^delcart/(\d+)/$', views.delcart, name="delcart"),
    # 清空购物车
    url(r'^clearcart/$', views.clearcart, name="clearcart"),
    # 改变购物车中的商品数量
    url(r'^changenum/(\d+)/$', views.changenum, name="changenum"),

    # 得到不同类型的商品
    url(r'^diffcategory/(\d+)/$', views.diffcategory, name="diffcategory"),
    # 得到六种商品
    url(r'^allgoods/$', views.allgoods, name="allgoods"),
    # 创建订单
    url(r'^createmyorder/$', views.createmyorder, name="createmyorder"),
    url(r'^all/$', views.all, name="all"),


    url(r'^myorder/$', views.myorder, name="myorder"),
]