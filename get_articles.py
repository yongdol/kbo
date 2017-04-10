import datetime
from bs4 import BeautifulSoup
from selenium import webdriver

driver = webdriver.Chrome('/Users/yongjoolim/Downloads/chromedriver')
today = datetime.datetime.now().strftime("%Y%m%d")
url = 'http://sports.news.naver.com/kbo/news/index.nhn?view=text&type=team&team=OB&date=' + today

driver.get(url)
driver.implicitly_wait(3)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
# news_list_div = soup.select('div.news_list > ul > li > div.text')
# for news_list in news_list_div:
#     a_tag = news_list.find('a')
#     news_link = a_tag.get('href')
#     print(news_link)
#     news_title = news_list.select('a.title > span')
#     print(news_title)
#     news_contents = news_list.find('p')
#     print(news_contents)
# driver.quit()



news_list_div = soup.select('div.news_list > ul > li > div.text')
for news_list in news_list_div:
    a_tag = news_list.find('a')
    news_link = a_tag.get('href')
    print(news_link)
    news_title = news_list.find('a.title > span')
    print(news_title)
    news_contents = news_list.find('p')
    print(news_contents)
driver.quit()