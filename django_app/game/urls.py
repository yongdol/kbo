from django.conf.urls import url

from game import views
# from article.views import ArticleListView


urlpatterns = [
    url(r'^team/$', views.get_team_rank, name="get_team_rank"),
    url(r'^hitter/$', views.get_hitter_rank, name="get_hitter_rank"),
]
