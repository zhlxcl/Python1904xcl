from django.conf.urls import url
app_name = "comment"
from . import views
urlpatterns = [
    url(r'^comment/(\d+)/$',views.AddComment.as_view(),name="comment"),
]