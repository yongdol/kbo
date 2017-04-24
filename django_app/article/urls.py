from django.conf.urls import url

from article import views
# from article.views import ArticleListView


urlpatterns = [
    url(r'^(?P<team_id>\d+)/(?P<date>\d+)/$', views.get_article_list, name="get_article_list"),
]
