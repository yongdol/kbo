from bs4 import BeautifulSoup
from django.shortcuts import render
from selenium.webdriver.firefox import webdriver

from game.models import TeamRank


def get_team_rank(request):
    rank_data = TeamRank.objects.all()
    context = {
        'rank_data': rank_data,
    }
    return render(request, 'game/rank.html', context)

