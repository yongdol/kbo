from django.conf.urls import url

from game import views
# from article.views import ArticleListView


urlpatterns = [
    url(r'^$', views.get_team_rank, name="get_team_rank"),
]
