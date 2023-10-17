# -*- coding: utf-8 -*-

import requests
from enum import Enum
from bs4 import BeautifulSoup
from util import Aspect, Star, House
from util import *
from marriage_report_logic import *

need_debug = True

if __name__ == '__main__':
    customer_name = 'lisha'

    name, birthday, location, glon_deg, glat_deg, toffset, is_dst, _ = load_customer_info(customer_name=customer_name)
    load_knowledge_file()
    load_knowledge_data_old()
    load_jobs_file()

    # 从爱星盘字典获取dist
    dist = load_ixingpan_area(user_input=location)
    # exit(0)

    """ ixingpan Http Result. """
    soup_ixingpan = fetch_ixingpan_soup(name=name, dist=dist, birthday_time=birthday, dst=is_dst, female=1)

    # 若未指定经纬度信息, 则用ixingpan结果中的
    if glon_deg == '' or glat_deg == '':
        glon_deg, glat_deg = parse_glon_glat(soup=soup_ixingpan)

    debug_msg = f'姓名:{name} \n位置信息:{location} \n出生信息:{birthday} \n经纬度信息:{glon_deg} {glat_deg} \n时区:{toffset} \n是否夏令时:{is_dst} \ndist:{dist}\n'
    print(debug_msg)

    """ almuten Http Result. """
    # print(f'glon_deg:{glon_deg}\tglat_deg:{glat_deg}')
    post_data = build_almuten_http_data(name=name, birthinfo=birthday, loc=location, glon_deg=glon_deg, glat_deg=glat_deg, toffset=toffset, is_dst=is_dst)
    soup_almuten = fetch_almuten_soup(post_data)
    parse_almuten_star(soup_almuten)
    parse_almuten_house()

    # 解析爱星盘结果
    parse_ixingpan_star(soup_ixingpan)
    parse_ixingpan_house(soup_ixingpan)
    parse_ixingpan_aspect(soup_ixingpan)

    get_square()
    get_house_energy()

    parse_love()
    parse_marrage_2()
    parse_marrage()
    parse_wealth()
    parse_health()
    parse_work()
    parse_asc_star()
    parse_study()
    parse_nature()

    # -------------------------- Print Trace Log ----------------------
    out_filename = f'./out/{customer_name}_out.txt'
    with open(out_filename, 'w') as f:
        f.writelines(f'\n『盘主信息』:\n')
        f.writelines(f'{debug_msg}')

        key_vec = ['个性显现及生活领域上的重点', '恋爱', '婚姻', '财富', '事业', '健康', '学业', '性格分析']

        for key in key_vec:
            if key not in all_trace_dict:
                continue

            field_dict = all_trace_dict[key]

            f.writelines(f'\n--------------------------- 解析「{key}」---------------------------')
            for biz, sub_vec in field_dict.items():
                f.writelines(f'\n『{biz}』:\n')
                # print(f'\n『{biz}』:')
                for index, sub in enumerate(sub_vec, start=1):
                    # print(f'{index}、{sub}')
                    f.writelines(f'{index}、{sub}\n')


        if need_debug:
            # f.writelines(common_trace_vec)
            # print('\n')

            f.writelines(f'\n『宫主飞星』:\n')
            for star, star_obj in star_dict.items():
                f.writelines(f'{star_obj}\n')
                # print(f'{star_obj}')

            # print('\n')
            f.writelines('\n')
            f.writelines(f'\n『宫位信息』:\n')
            house_sorted_dict = dict(sorted(house_dict.items(), key=lambda x: x[0]))
            for house_num, house_obj in house_sorted_dict.items():
                # print(house_obj)
                f.writelines(f'{house_obj}\n')
