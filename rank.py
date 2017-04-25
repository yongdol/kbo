import datetime

import sqlite3
from bs4 import BeautifulSoup
from django.shortcuts import render
from selenium import webdriver


def get_team_rank():
    driver = webdriver.Firefox()
    base_url = 'http://www.koreabaseball.com/TeamRank/TeamRank.aspx'
    driver.get(base_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    standard_date = datetime.datetime.now().strftime("%Y") + soup.select('span.exp2')[0].text

    rank_table_list = soup.select('table.tData > tbody > tr')[0:10]
    con = sqlite3.connect("./django_app/db.sqlite3")
    cur = con.cursor()
    for data in rank_table_list:
        rank_bs_tag = data.find('td')
        rank = rank_bs_tag.text

        team_bs_tag = rank_bs_tag.next_sibling.next_sibling
        team = team_bs_tag.text
        if team == "두산":
            team_id = "1"
        elif team == "NC":
            team_id = "2"
        elif team == "넥센":
            team_id = "3"
        elif team == "LG":
            team_id = "4"
        elif team == "KIA":
            team_id = "5"
        elif team == "SK":
            team_id = "6"
        elif team == "한화":
            team_id = "7"
        elif team == "롯데":
            team_id = "8"
        elif team == "삼성":
            team_id = "9"
        else:
            team_id = "10"

        win_bs_tag = team_bs_tag.next_sibling.next_sibling
        win = win_bs_tag.text

        lose_bs_tag = win_bs_tag.next_sibling.next_sibling
        lose = lose_bs_tag.text

        draw_bs_tag = lose_bs_tag.next_sibling.next_sibling
        draw = draw_bs_tag.text

        win_rate_bs_tag = draw_bs_tag.next_sibling.next_sibling
        win_rate = win_rate_bs_tag.text

        game_gap_bs_tag = win_rate_bs_tag.next_sibling.next_sibling
        game_gap = game_gap_bs_tag.text

        recent_10_game_bs_tag = game_gap_bs_tag.next_sibling.next_sibling
        recent_10_game = recent_10_game_bs_tag.text

        continuous_bs_tag = recent_10_game_bs_tag.next_sibling.next_sibling
        continuous = continuous_bs_tag.text

        home_score_bs_tag = continuous_bs_tag.next_sibling.next_sibling
        home_score = home_score_bs_tag.text

        away_score_bs_tag = home_score_bs_tag.next_sibling.next_sibling
        away_score = away_score_bs_tag.text

        # cur.execute("INSERT OR IGNORE INTO game_teamrank (team_id, rank, win, lose, draw, win_rate, game_gap,\
        # recent_10_game, continuous, home_score, away_score, standard_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
        #  ?, ?)", (team_id, rank, win, lose, draw, win_rate, game_gap, recent_10_game, continuous, home_score, away_score, standard_date))
        # con.commit()

    cur.close()
    driver.quit()

get_team_rank()
