import datetime
from time import sleep

from crawling import team_list
import sqlite3
from bs4 import BeautifulSoup
from selenium import webdriver

# today = datetime.datetime.now().strftime("%Y%m%d")
today = '20170427'


def find_next(tagname):
    return tagname.next_sibling.next_sibling


def save_team_rank():
    driver = webdriver.Firefox()
    base_url = 'http://www.koreabaseball.com/TeamRank/TeamRank.aspx'
    driver.get(base_url)
    # prev_date rank
    # driver.find_element_by_id('cphContents_cphContents_cphContents_btnPreDate').click()
    # sleep(5)

    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    standard_date_tag = soup.select('span.stand')[0].text.replace(' ', '')
    standard_date = standard_date_tag[:4] + standard_date_tag[5:7] + standard_date_tag[8:10]


    rank_table_list = soup.select('table.tData > tbody > tr')[0:10]
    con = sqlite3.connect("./django_app/db.sqlite3")
    cur = con.cursor()

    for data in rank_table_list:
        rank_bs_tag = data.find('td')
        rank = rank_bs_tag.text

        team_bs_tag = find_next(rank_bs_tag)
        team = team_bs_tag.text.upper()
        for i in range(0, len(team_list)):
            if team == team_list[i]['short_name']:
                team_id = i + 1
            else:
                pass

        win_bs_tag = find_next(team_bs_tag)
        win = win_bs_tag.text

        lose_bs_tag = find_next(win_bs_tag)
        lose = lose_bs_tag.text

        draw_bs_tag = find_next(lose_bs_tag)
        draw = draw_bs_tag.text

        win_rate_bs_tag = find_next(draw_bs_tag)
        win_rate = win_rate_bs_tag.text

        game_gap_bs_tag = find_next(win_rate_bs_tag)
        game_gap = game_gap_bs_tag.text

        recent_10_game_bs_tag = find_next(game_gap_bs_tag)
        recent_10_game = recent_10_game_bs_tag.text

        continuous_bs_tag = find_next(recent_10_game_bs_tag)
        continuous = continuous_bs_tag.text

        home_score_bs_tag = find_next(continuous_bs_tag)
        home_score = home_score_bs_tag.text

        away_score_bs_tag = find_next(home_score_bs_tag)
        away_score = away_score_bs_tag.text

        cur.execute("INSERT OR IGNORE INTO game_teamrank (team_id, rank, win, lose, draw, win_rate, game_gap,\
        recent_10_game, continuous, home_score, away_score, standard_date) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?,\
         ?, ?)", (team_id, rank, win, lose, draw, win_rate, game_gap, recent_10_game, continuous, home_score, away_score, standard_date))
        con.commit()

    cur.close()

    driver.quit()


def save_hitter_rank():
    driver = webdriver.Firefox()
    first_url = 'http://www.koreabaseball.com/Record/Player/HitterBasic/Basic1.aspx'
    second_url = 'http://www.koreabaseball.com/Record/Player/HitterBasic/Basic2.aspx'
    driver.get(first_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    hitter_rank_table_first_list = soup.select('table.tData01.tt > tbody > tr')[0:30]
    # print(hitter_rank_table_first_list)

    driver.get(second_url)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')
    hitter_rank_table_two_list = soup.select('table.tData01.tt > tbody > tr')[0:30]
    # print(hitter_rank_table_two_list)

    con = sqlite3.connect("./django_app/db.sqlite3")
    cur = con.cursor()
    hitter_rank_first_data = []
    hitter_rank_second_data = []


    for data in hitter_rank_table_first_list:

        rank_bs_tag = data.find('td')
        player_bs_tag = find_next(rank_bs_tag)
        player = player_bs_tag.text
        team_bs_tag = find_next(player_bs_tag)
        team = team_bs_tag.text.upper()
        for i in range(0, len(team_list)):
            if team == team_list[i]['short_name']:
                team_id = i + 1
            else:
                pass

        avg_bs_tag = find_next(team_bs_tag)
        avg = avg_bs_tag.text
        g_bs_tag = find_next(avg_bs_tag)
        g = g_bs_tag.text
        pa_bs_tag = find_next(g_bs_tag)
        pa = pa_bs_tag.text
        ab_bs_tag = find_next(pa_bs_tag)
        ab = ab_bs_tag.text
        r_bs_tag = find_next(ab_bs_tag)
        r = r_bs_tag.text
        h_bs_tag = find_next(r_bs_tag)
        h = h_bs_tag.text
        two_base_bs_tag = find_next(h_bs_tag)
        two_base = two_base_bs_tag.text
        three_base_bs_tag = find_next(two_base_bs_tag)
        three_base = three_base_bs_tag.text
        hr_base_bs_tag = find_next(three_base_bs_tag)
        hr = hr_base_bs_tag.text
        total_base_bs_tag = find_next(hr_base_bs_tag)
        total_base = total_base_bs_tag.text
        rbi_bs_tag = find_next(total_base_bs_tag)
        rbi = rbi_bs_tag.text
        sac_bs_tag = find_next(rbi_bs_tag)
        sac = sac_bs_tag.text
        sf_bs_tag = find_next(sac_bs_tag)
        sf = sf_bs_tag.text
        hitter_rank_first_data.append(
            {
                "player": player,
                "team_id": team_id,
                "avg": avg,
                "g": g,
                "pa": pa,
                "ab": ab,
                "r": r,
                "h": h,
                "two_base": two_base,
                "three_base": three_base,
                "hr": hr,
                "total_base": total_base,
                "rbi": rbi,
                "sac": sac,
                "sf": sf,
            }
        )
    # print(hitter_rank_first_data)

    for data in hitter_rank_table_two_list:
        rank_bs_tag = data.find('td')

        bb_bs_tag = find_next(find_next(find_next(find_next(rank_bs_tag))))
        bb = bb_bs_tag.text
        ibb_bs_tag = find_next(bb_bs_tag)
        ibb = ibb_bs_tag.text
        hbp_bs_tag = find_next(ibb_bs_tag)
        hbp = hbp_bs_tag.text
        so_bs_tag = find_next(hbp_bs_tag)
        so = so_bs_tag.text
        gdp_bs_tag = find_next(so_bs_tag)
        gdp = gdp_bs_tag.text
        slg_bs_tag = find_next(gdp_bs_tag)
        slg = slg_bs_tag.text
        obp_bs_tag = find_next(slg_bs_tag)
        obp = obp_bs_tag.text
        ops_bs_tag = find_next(obp_bs_tag)
        ops = ops_bs_tag.text
        mh_bs_tag = find_next(ops_bs_tag)
        mh = mh_bs_tag.text
        risp_bs_tag = find_next(mh_bs_tag)
        risp = risp_bs_tag.text
        ph_ba_bs_tag = find_next(risp_bs_tag)
        ph_ba = ph_ba_bs_tag.text

        hitter_rank_second_data.append(
            {
                "bb": bb,
                "ibb": ibb,
                "hbp": hbp,
                "so": so,
                "gdp": gdp,
                "slg": slg,
                "obp": obp,
                "ops": ops,
                "mh": mh,
                "risp": risp,
                "ph_ba": ph_ba,
                "standard_date": today,
            }
        )
    # print(hitter_rank_second_data)

    for i in range(0, len(hitter_rank_first_data)):
        hitter_rank_first_data[i]['bb'] = hitter_rank_second_data[i]['bb']
        hitter_rank_first_data[i]['ibb'] = hitter_rank_second_data[i]['ibb']
        hitter_rank_first_data[i]['hbp'] = hitter_rank_second_data[i]['hbp']
        hitter_rank_first_data[i]['so'] = hitter_rank_second_data[i]['so']
        hitter_rank_first_data[i]['gdp'] = hitter_rank_second_data[i]['gdp']
        hitter_rank_first_data[i]['slg'] = hitter_rank_second_data[i]['slg']
        hitter_rank_first_data[i]['obp'] = hitter_rank_second_data[i]['obp']
        hitter_rank_first_data[i]['ops'] = hitter_rank_second_data[i]['ops']
        hitter_rank_first_data[i]['mh'] = hitter_rank_second_data[i]['mh']
        hitter_rank_first_data[i]['risp'] = hitter_rank_second_data[i]['risp']
        hitter_rank_first_data[i]['ph_ba'] = hitter_rank_second_data[i]['ph_ba']


        player = hitter_rank_first_data[i]['player']
        team_id = hitter_rank_first_data[i]['team_id']
        avg = hitter_rank_first_data[i]['avg']
        g = hitter_rank_first_data[i]['g']
        pa = hitter_rank_first_data[i]['pa']
        ab = hitter_rank_first_data[i]['ab']
        r = hitter_rank_first_data[i]['r']
        h = hitter_rank_first_data[i]['g']
        two_base = hitter_rank_first_data[i]['two_base']
        three_base = hitter_rank_first_data[i]['three_base']
        hr = hitter_rank_first_data[i]['hr']
        total_base = hitter_rank_first_data[i]['total_base']
        rbi = hitter_rank_first_data[i]['rbi']
        sac = hitter_rank_first_data[i]['sac']
        sf = hitter_rank_first_data[i]['sf']
        bb = hitter_rank_first_data[i]['bb']
        ibb = hitter_rank_first_data[i]['ibb']
        hbp = hitter_rank_first_data[i]['hbp']
        so = hitter_rank_first_data[i]['so']
        gdp = hitter_rank_first_data[i]['gdp']
        slg = hitter_rank_first_data[i]['slg']
        obp = hitter_rank_first_data[i]['obp']
        ops = hitter_rank_first_data[i]['ops']
        mh = hitter_rank_first_data[i]['mh']
        risp = hitter_rank_first_data[i]['risp']
        ph_ba = hitter_rank_first_data[i]['ph_ba']
        standard_date = hitter_rank_second_data[i]['standard_date']

        cur.execute("INSERT OR IGNORE INTO game_hiterrank (player, team_id, avg, g, pa, ab, r, h, two_base, three_base,\
        hr, total_base, rbi, sac, sf, bb, ibb, hbp, so, gdp, slg, obp, ops, mh, risp, ph_ba, standard_date) \
        VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", (player,
        team_id, avg, g, pa, ab, r, h, two_base, three_base, hr, total_base, rbi, sac, sf, bb, ibb, hbp, so, gdp, slg,
        obp, ops, mh, risp, ph_ba, standard_date))
        con.commit()
    # print(hitter_rank_first_data)

    driver.quit()

# save_team_rank()
save_hitter_rank()
