# 导入url路由模块
from django.conf.urls import url
# 导入视图函数模块
from . import views

app_name = "myvote"

# 应用路由配置
urlpatterns = [
    url(r'^$',views.index,name="index"),
    url(r'^choicelist/(\d+)/$',views.choicelist,name="choicelist"),
    url(r'^choiceresult/(\d+)/$',views.choiceresult,name="choiceresult"),
    url(r'^login/$',views.login,name="login"),
]