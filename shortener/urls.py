from django.conf.urls import url
from . import views

app_name="shortener"

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name="index"),
    url(r'^(?P<shorturl>[\w-]+)/$', views.URLRedirect.as_view() , name="view"),
]
