import json
import os

import re
from bs4 import BeautifulSoup
import requests

team_dict = {'HH': '7'}
today = '20170410'


def make_article_file():
    for team, team_id in team_dict.items():
        template_dir = './django_app/templates/articles/' + team + '/'
        file_name = template_dir + today + '_' + team + "_test.txt"
        base_url = 'http://sports.news.naver.com/kbo/news/index.nhn?view=text&type=team&team=' + team + '&date=' + today
        data = requests.get(base_url)
        html_doc = BeautifulSoup(data.text, 'lxml')

        # Parsing (total pages)
        match = re.search("totalPages\":.", html_doc.text)
        total_page = int(match.group(0).split(":")[1])

        # soup = str(BeautifulSoup(html_doc.text, 'lxml')).split('\n')
        # f = open(file_name, 'w+')
        # f.write(soup)
        # for line in soup:
        #     if line.__contains__("newsListModel"):
        #         article_str = line.strip().replace('newsListModel: ', '')
        #         print(article_str)
        #         print(type(article_str))
                # article_dic = dict(article_str)
                # print(article_dic)
                # print(type(article_dic))
                # for i in range(len(article_dic["list"])):
                #     print(i)
                # f.write(article_dic)
                # else:
                #     pass
        # f.close()

make_article_file()


# def save_article():