
# 导入url路由模块
from django.conf.urls import url
# 导入视图函数模块
from . import views

app_name = "booktest"

# 应用路由配置
urlpatterns = [
    # 访问对应的路由可以执行对应的视图函数
    # 使用视图方法
    # url(r'^$',views.index,name="index"),
    # 使用视图类
    # url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^$',views.IndexTemplateView.as_view(),name="index"),

    # url(r'^list/$',views.list,name="list"),
    url(r'^list/$',views.ListView.as_view(),name="list"),

    url(r'^detail/(\d+)/$',views.detail,name="detail"),

    url(r'^deletebook/(\d+)/$',views.deletebook,name="deletebook"),
    url(r'^deletehero/(\d+)/$',views.deletehero,name="deletehero"),

    url(r'^addbook/$',views.addbook,name="addbook"),
    url(r'^addhero/(\d+)/$',views.addhero,name="addhero"),
]


"""
解除硬编码
    硬编码：在静态文件写入超级链接的绝对路径
    缺点：当路由地址发生变化。所有绝对路径编写的超级链接都需要更改。解除硬编码可以避免绝对路径
    
    1.使用应用命名空间
    2.使用路由的名字

"""