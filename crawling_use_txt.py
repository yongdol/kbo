import os

from bs4 import BeautifulSoup
import requests

team_dict = {'HH': '7'}
today = '20170410'


def crawling_data_make_file():
    for team, team_id in team_dict.items():
        template_dir = './django_app/templates/articles/' + team + '/'
        file_name = template_dir + today + '_' + team + "_test.txt"
        url = 'http://sports.news.naver.com/kbo/news/index.nhn?view=text&type=team&team=' + team + '&date=' + today
        html_doc = requests.get(url)
        # print(html_doc)
        soup = str(BeautifulSoup(html_doc.text, 'lxml'))
        f = open(file_name, 'w')
        f.write(soup)
        f.close()




crawling_data_make_file()
