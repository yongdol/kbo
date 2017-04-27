import datetime
from bs4 import BeautifulSoup
from django.core.serializers import json
from django.shortcuts import render
from selenium.webdriver.firefox import webdriver

from article.models import Team, Article
from game.models import Teamrank, Hiterrank


def get_team_rank(request):
    today = datetime.datetime.now().strftime("%Y%m%d")
    today = 20170427
    # rank_data = Teamrank.objects.filter(standard_date=today)
    all_rank_data = Teamrank.objects.all()

    rank_data = all_rank_data.filter(standard_date=today)
    team_data = Team.objects.all()
    standard_date = Teamrank.objects.values_list('standard_date', flat=True).distinct().order_by('standard_date')

    context = {
        'rank_data': rank_data,
        'team_data': team_data,
        'standard_date': standard_date,
        'all_rank_data': all_rank_data,
        'today': today,
    }
    return render(request, 'game/team_rank.html', context)


def get_hitter_rank(request):
    hitter_rank_data = Hiterrank.objects.all()
    homerun_rank_data = hitter_rank_data.order_by('hr')
    team_data = Team.objects.all()
    context = {
        'hitter_rank_data': hitter_rank_data,
        'homerun_rank_data': homerun_rank_data,
        'team_data': team_data,
    }
    return render(request, 'game/hitter.html', context)
