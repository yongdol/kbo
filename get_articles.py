import datetime
import sqlite3
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver


# team_list = ['OB', 'NC', 'WO', 'LG', 'HT', 'SK', 'HH', 'LT', 'SS', 'KT']

# driver = webdriver.Chrome('/Users/yongjoolim/Downloads/chromedriver')
# driver = webdriver.Firefox()
# # today = datetime.datetime.now().strftime("%Y%m%d")
today = '20170410'

con = sqlite3.connect("./django_app/db.sqlite3")
cur = con.cursor()
# for team in team_list:
#     template_dir = './django_app/templates/articles/' + team + '/'
#     file_name = template_dir + today + '_' + team + ".txt"
    # url = 'http://sports.news.naver.com/kbo/news/index.nhn?view=text&type=team&team=' + team + '&date=' + today
    # driver.get(url)
    # driver.implicitly_wait(5)
    # html = driver.page_source
    # soup = BeautifulSoup(html, 'html.parser')
    # news_list_div = soup.select('div.news_list > ul > li > div.text')
    # f = open(file_name, 'w')
    # for news_list in news_list_div:
    #     a_tag = news_list.find('a')
    #     news_link = a_tag.get('href')
    #     news_title = str(a_tag.find('span')).replace('<span>', '').replace('</span>', '')
    #     news_contents = str(news_list.find('p')).replace('<p class="desc">', '').replace('</p>', '')
    #     row = news_title + '\t' + news_contents + '\t' + news_link + '\n'
    #     f.write(row)
    # print(news_link)
    # print(type(news_title))
    # print(news_title)
    # print(type(news_contents))
    # print(news_contents)
    # sleep(3)

    # driver.quit()
    # f.close()
team_dict = {'OB': '1', 'NC': '2', 'WO': '3', 'LG': '4'}
for team, team_id in team_dict.items():
    template_dir = './django_app/templates/articles/' + team + '/'
    file_name = template_dir + today + '_' + team + ".txt"
    f = open(file_name, 'r')
    lists = f.readlines()
    for lines in lists:
        line = lines.strip()
        title = line.split('\t')[0]
        contents = line.split('\t')[1]
        link = line.split('\t')[2]
        # print(team)
        # print(team_id)
    # print(title)
    # print(contents)
    # print(link)
        cur.execute('INSERT OR IGNORE INTO article_article (team_id, title, contents, link, date) VALUES(?, ?, ?, ?, ?)', (team_id, title, contents, link, today))
        con.commit()
f.close()
cur.close()
