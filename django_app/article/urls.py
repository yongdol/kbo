from django.conf.urls import url
from django.views.generic import TemplateView

from article.views import ArticleListView
from . import views


urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name="kbo/index.html")),
    url(r'^article/(?P<team_id>\d+)/$', ArticleListView.as_view()),
]
