from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^article/(?P<team_id>[0-9]+)/$', views.get_articles, name='articles'),
]
