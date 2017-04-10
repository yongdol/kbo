import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/yongjoolim/Downloads/chromedriver')
today = datetime.datetime.now().strftime("%Y%m%d")
url = 'http://sports.news.naver.com/kbo/news/index.nhn?view=text&type=team&team=OB&date=' + today
url = 'http://sports.news.naver.com/kbo/news/index.nhn?view=text&type=team&team=OB&date=20170410'

driver.get(url)
driver.implicitly_wait(3)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
news_list_div = soup.select('div.news_list > ul > li > div.text')
TEMPLATES_DIR = './django_app/templates/articles/OB/'
f = open(TEMPLATES_DIR + today + ".txt", 'w')
for news_list in news_list_div:
    a_tag = news_list.find('a')
    news_link = a_tag.get('href')
    news_title = str(a_tag.find('span'))[6:][:-7]
    # news_title = str(a_tag.find('span')).replace('<span>', '').replace('</span>', '')
    news_contents = str(news_list.find('p'))[16:][:-4]
    # news_contents = str(news_list.find('p')).replace('<p class="desc">', '').replace('</p>', '')
    row = news_title + '\t' + news_contents + '\t' + news_link + '\n'
    # print(row)
    f.write(row)
    # print(news_link)
    # print(type(news_title))
    # print(news_title)
    # print(type(news_contents))
    # print(news_contents)
f.close()

driver.quit()