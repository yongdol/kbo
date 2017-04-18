from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<team>\w+)/$', views.get_articles, name='articles'),
]
