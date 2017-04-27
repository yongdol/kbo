import datetime
import json
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver

team_list = [
            {'full_name': '두산베어스', 'short_name': '두산', 'nick_name': 'OB', 'id': '1'},
            {'full_name': '엔씨다이노스', 'short_name': 'NC', 'nick_name': 'NC', 'id': '2'},
            {'full_name': '넥센히어로즈', 'short_name': '넥센', 'nick_name': 'WO', 'id': '3'},
            {'full_name': '엘지트윈스', 'short_name': 'LG', 'nick_name': 'LG', 'id': '4'},
            {'full_name': '기아타이거스', 'short_name': 'KIA', 'nick_name': 'HT', 'id': '5'},
            {'full_name': '에스케이와이번스', 'short_name': 'SK', 'nick_name': 'SK', 'id': '6'},
            {'full_name': '한화이글스', 'short_name': '한화', 'nick_name': 'HH', 'id': '7'},
            {'full_name': '롯데자이언츠', 'short_name': '롯데', 'nick_name': 'LT', 'id': '8'},
            {'full_name': '삼성라이온즈', 'short_name': '삼성', 'nick_name': 'SS', 'id': '9'},
            {'full_name': '케이티위즈', 'short_name': 'KT', 'nick_name': 'KT', 'id': '10'}
]

today = datetime.datetime.now().strftime("%Y%m%d")
# today = '20170423'


def save_team():
    con = sqlite3.connect("./django_app/db.sqlite3")
    cur = con.cursor()
    for i in range(0, len(team_list)):
        full_name = team_list[i]['full_name']
        short_name = team_list[i]['short_name']
        nick_name = team_list[i]['nick_name']
        cur.execute("INSERT INTO article_team (full_name, short_name, nick_name) VALUES(?, ?, ?)", (full_name, short_name, nick_name))
        con.commit()
    cur.close()


# crawling article and make file
def crawling_data_make_file():
    # driver = webdriver.PhantomJS()
    driver = webdriver.Firefox()
    for i in range(0, len(team_list)):
        article_data = []
        team = team_list[i]['nick_name']
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
    for i in range(0, len(team_list)):
        team = team_list[i]['nick_name']
        team_id = i + 1
        # team_id = 10
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


# save_team()
crawling_data_make_file()
save_data()
