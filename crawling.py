import datetime
import json
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver


team_dict = {
    'OB': '1',
    'NC': '2',
    'WO': '3',
    'LG': '4',
    'HT': '5',
    'SK': '6',
    'HH': '7',
    'LT': '8',
    'SS': '9',
    'KT': '10'
}
# team_dict = {'KT': '10'}
today = datetime.datetime.now().strftime("%Y%m%d")
# today = '20170425'


# crawling article and make file
def crawling_data_make_file():
    # driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    for team, team_id in team_dict.items():
        article_data = []
        template_dir = './django_app/templates/articles/' + team + '/'
        file_name = template_dir + today + '_' + team + ".txt"
        base_url = 'http://sports.news.naver.com/kbo/news/index.nhn?view=text&type=team&team=' + team + '&date=' + today
        driver.get(base_url)
        html = driver.page_source
        soup = BeautifulSoup(html, 'html.parser')

        # total page check
        total_page = len(soup.select('div.paginate > a'))

        for page in range(1, total_page + 2):
            target_url = base_url + '&page=' + str(page)
            print(target_url)
            driver.get(target_url)
            html = driver.page_source
            soup = BeautifulSoup(html, 'html.parser')
            news_list_div = soup.select('div.news_list > ul > li')
            for news_list in news_list_div:
                news_link = "http://sports.news.naver.com" + news_list.find('a').get('href')
                news_title = news_list.find('div').text.split('\n')[1]
                news_contents = news_list.find('div').text.split('\n')[2]
                news_img = news_list.find('img')

                # img check
                if news_img is None:
                    news_img = "None"
                else:
                    news_img = news_img.get('src')

                article_data.append(
                    {"title": news_title,
                     "contents": news_contents,
                     "link": news_link,
                     "date": today,
                     "img": news_img,
                     }
                )

        with open(file_name, 'w') as outfile:
            json.dump(article_data, outfile, ensure_ascii=False)

    driver.quit()


def save_data():
    # sqlite3 connect
    con = sqlite3.connect("./django_app/db.sqlite3")
    cur = con.cursor()
    for team, team_id in team_dict.items():
        template_dir = './django_app/templates/articles/' + team + '/'
        file_name = template_dir + today + '_' + team + ".txt"
        f = open(file_name, 'r')
        article_list = f.readlines()
        for article in article_list:
            article_dict = json.loads(article)
            for i in range(0, len(article_dict)):
                title = article_dict[i]["title"]
                contents = article_dict[i]["contents"]
                link = article_dict[i]["link"]
                date = article_dict[i]["date"]
                img = article_dict[i]["img"]
                cur.execute("INSERT OR IGNORE INTO article_article (team_id, title, contents, link, date, img) \
                    VALUES(?, ?, ?, ?, ?, ?)", (team_id, title, contents, link, date, img))
                con.commit()
        f.close()
    cur.close()


crawling_data_make_file()
save_data()
