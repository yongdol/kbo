from django.shortcuts import render
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
from article.models import Article, Team, OB


def index(request):
    return render(request, 'kbo/index.html')


def get_articles(request, team):
    print(team)
    articles = Team.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/article_list.html', context)
