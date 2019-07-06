
from django.conf.urls import url
from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^$',views.index,name='index'),
    url(r'^choicelist/(\d+)/$',views.choicelist,name='choicelist'),
    url(r'^result/(\d+)/$',views.result,name='result'),
]

