from django.conf.urls import url
from . import views

app_name = 'gift'

urlpatterns = [
    url(r'^login/$',views.LoginView.as_view(),name="login"),
    url(r'^regist/$',views.RegistView.as_view(),name="regist"),
]