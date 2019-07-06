
# 导入url路由模块
from django.conf.urls import url
# 导入视图函数模块
from . import views
app_name = "book"
# 应用路由配置
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^list/$',views.list,name="list"),
    url(r'^detail/(\d+)/$',views.detail,name="detail"),
    url(r'^addbook/$',views.addbook,name="addbook"),
    url(r'^deletebook/(\d+)/$',views.deletebook,name="deletebook"),
    url(r'^addhero/(\d+)/$',views.addhero,name="addhero"),
    url(r'^deletehero/(\d+)/$',views.deletehero,name="deletehero"),
]