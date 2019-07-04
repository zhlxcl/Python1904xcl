"""demo1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path

# 导入url路由模块和include模块
from django.conf.urls import url,include



# 项目根路由：用户在浏览器中输入的网址需要和路由匹配
urlpatterns = [
    path('admin/', admin.site.urls),
    # 在项目根路由下通过url以及include指明应用路由的配置文件
    url('',include('booktest.urls',namespace="booktest")),
]


"""
匹配（参数问题）：
1.输入网址格式需要和路由有列表格式匹配（）
2.路由列表格式需要和视图函数格式匹配（）
"""