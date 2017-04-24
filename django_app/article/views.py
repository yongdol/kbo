import datetime

from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from article.models import Article


def index(request):
    today = datetime.datetime.now().strftime("%Y%m%d")
    # today = 20170410
    return render(request, 'kbo/index.html', {'today': today})


def get_article_list(request, team_id, date):
    articles = Article.objects.filter(team_id=team_id, date=date).order_by('id')
    dates = Article.objects.values_list('date', flat=True).distinct().order_by('date')
    today = datetime.datetime.now().strftime("%Y%m%d")
    # today = 20170410
    # pagination
    page = request.GET.get('page', 1)
    paginator = Paginator(articles, 12)
    try:
        articles = paginator.page(page)
    except PageNotAnInteger:
        articles = paginator.page(1)
    except EmptyPage:
        articles = paginator.page(paginator.num_pages)

    context = {
        'articles': articles,
        'dates': dates,
        'today': today,
        'team_id': team_id,
    }

    return render(request, 'articles/article_list.html', context)
