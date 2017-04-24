from django.views.generic import ListView, DetailView
from article.models import Article

# today = datetime.datetime.now().strftime("%Y%m%d")
today = 20170410


class ArticleListView(ListView):
    model = Article
    template_name = 'articles/article_list.html'
    context_object_name = 'articles'
    paginate_by = 20

    def get_queryset(self):
        return Article.objects.filter(team_id=self.kwargs['team_id'], date=today).order_by('id')


