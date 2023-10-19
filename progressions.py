# -*- coding: utf-8 -*-
from typing import Tuple

import requests
from enum import Enum
from bs4 import BeautifulSoup
from util import Aspect, Star, House
from util import *
from util import marriage_trace_dict
import datetime
from run import name, birthday, location, cur_loc, glon_deg, glat_deg, toffset, is_dst, dist




def get_solar_return(duration=10):
    # https://xp.ixingpan.com/xp.php?type=solarreturn&name=jackietan&sex=0&province=山东省&city=济南市&dist=1550&date=1989-08-05&time=12:58&tz=8.00&dst=1&hsys=P&date2=2026-10-18&time2=17:32
    # url = 'https://xp.ixingpan.com/xp.php?type=solarreturn&name=刘行&sex=1&dist=1550&date=1992-12-27&time=05:30&dst=0&date2=2025-08-17&time2=14:09&hsys=P&dist2=1867'
    # https://xp.ixingpan.com/xp.php?type=solarreturn&name=%E5%88%98%E8%A1%8C&sex=1&dist=1550&date=1992-12-27&time=05:30&dst=0&date2=2025-08-17&time2=14:09&hsys=P&dist2=1867
    def _get_solar_url_param():
        logger.debug(cur_loc)
        dist2 = load_ixingpan_area(user_input=cur_loc)
        logger.debug(f'获取日返的dist2={dist2}')

        date1 = birthday.split(' ')[0]
        time2 = birthday.split(' ')[1]  # 20:00

        return dist2, time2, date1

    def _modify_date(date_str):
        # 将字符串转换为日期对象
        date = datetime.datetime.strptime(date_str, "%Y-%m-%d")

        # 增加一个月
        modified_date = date + datetime.timedelta(days=31)

        # 修改年份
        current_year = datetime.datetime.now().year
        modified_date = modified_date.replace(year=current_year)

        # 返回之后的10年的字符串
        result = []
        for i in range(11):
            result.append(modified_date.strftime("%Y-%m-%d"))
            modified_date = modified_date.replace(year=modified_date.year + 1)

        return result

    dist2, time2, date1 = _get_solar_url_param()

    base_url = 'https://xp.ixingpan.com/xp.php?'
    date2_vec = _modify_date(date_str=birthday.split(' ')[0])
    for date2 in date2_vec:
        query_params = {
            'type': 'solarreturn',
            'name': name,
            'sex': 1,
            'dist': dist,
            'date': date1,
            'time': time2,
            'dst': is_dst,
            'date2': date2,
            'time2': time2,
            'hsys': 'P',
            'dist2': dist2
        }

        url = f'{base_url}{"&".join(f"{k}={v}" for k, v in query_params.items())}'
        logger.debug(f'日返url，{url}')

    # response = requests.get(url, cookies={'xp_planets_natal': '0,1,2,3,4,5,6,7,8,9,25,26,27,28,15,19,10,29'})
    #
    # # 获取返回的HTML源码
    # html_str = response.text
    # soup = BeautifulSoup(html_str, 'html.parser')


def test():
    # logger.debug('test haaaaaaaaaaaaaaaaa')

    report.set_msg('A', 'a', 'a1')
    report.set_msg('A', 'a', 'a12')
    report.set_msg('A', 'aa', 'a2')
    report.set_msg('A', 'aa', 'a3')
    report.set_msg('B', 'b', 'b1')
    report.set_msg('B', 'bb', 'b2')
    # print(report)

if __name__ == '__main__':
    get_solar_return()
    # pass