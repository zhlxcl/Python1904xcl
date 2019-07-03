
# 导入url路由模块
from django.conf.urls import url
# 导入视图函数模块
from . import views

# 应用路由配置
urlpatterns = [
    url(r'^index/$',views.index),
    url(r'^list/$',views.list),
    url(r'^detail/$',views.detail),

]
