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

        if data:
            html_doc = BeautifulSoup(data.text, 'lxml')

            # Parsing (total pages)
            match = re.search("totalPages\":[0-9]", html_doc.text)
            total_page = int(match.group(0).split(":")[1])

            soup = str(html_doc).split('\n')





        else:
            print("please retry")





        # f = open(file_name, 'w+')
        # f.write(soup)
        # for line in soup:
        #     if line.__contains__("newsListModel"):
                # newsList
                # articles_str = line.strip().replace('newsListModel: {"list":', '').replace('"url":null', '').split("],\"")[0]
                # articles_str = line.strip().replace('newsListModel: {"list":', '')
                # articles_str = str(line.strip().split('\n'))
                # print(articles_str)
                # print(type(articles_str))

                # print(type(articles_str))
                # article_dic = dict(articles_str)
                # print(article_dic)
                # print(type(article_dic))
                # for i in range(len(article_dic["list"])):
                #     print(i)
                # f.write(articles_str)
                # else:
                #     pass
        # f.close()

make_article_file()


# def save_article():