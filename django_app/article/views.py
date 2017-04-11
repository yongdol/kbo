from django.shortcuts import render
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from article.models import Article, Team


def index(request):
    return render(request, 'kbo/index.html')


def get_articles(request, team_id):
    articles = Article.objects.filter(team_id=team_id)
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article_list.html', context)
