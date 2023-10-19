# -*- coding: utf-8 -*-

import requests
from enum import Enum
from bs4 import BeautifulSoup
from util import Aspect, Star, House
from util import *
from marriage_report_logic import *
from progressions import *
import os

need_debug = True

customer_name = 'jackietan'

name, birthday, location, cur_loc, glon_deg, glat_deg, toffset, is_dst, _ = load_customer_info(customer_name=customer_name)
dist = load_ixingpan_area(user_input=location)


def get_soup_from_http():
    global glon_deg, glat_deg

    folder_path = f'./cache_file/{customer_name}'
    os.makedirs(folder_path, exist_ok=True)

    """ ixingpan Http Result. 有 cache 文件则从文件加载，没有走 http 请求 """
    filename_ixingpan = f'./cache_file/{customer_name}/{customer_name}_ixingpan.pickle'

    if os.path.exists(filename_ixingpan):
        soup_ixingpan = dump_load_http_result(filename=filename_ixingpan, is_load_mode=True)
        logger.info(f'Load soup from File:{filename_ixingpan}')
    else:
        soup_ixingpan = fetch_ixingpan_soup(name=name, dist=dist, birthday_time=birthday, dst=is_dst, female=1)
        dump_load_http_result(filename=filename_ixingpan, soup_obj=soup_ixingpan, is_load_mode=False)
        logger.info(f'走Http请求获取爱星盘排盘信息，并且 Dump BeautifulSoup to File:{filename_ixingpan}')

    # Update glon_deg, glat_deg. 若未指定经纬度信息, 则用ixingpan结果中的
    if glon_deg == '' or glat_deg == '':
        glon_deg, glat_deg = parse_glon_glat(soup=soup_ixingpan)

    """ almuten Http Result. """
    filename_almuten = f'./cache_file/{customer_name}/{customer_name}_almuten.pickle'

    if os.path.exists(filename_almuten):
        soup_almuten = dump_load_http_result(filename=filename_almuten, is_load_mode=True)
        logger.info(f'Load soup from File:{filename_almuten}')
    else:
        post_data = build_almuten_http_data(name=name, birthinfo=birthday, loc=location, glon_deg=glon_deg, glat_deg=glat_deg, toffset=toffset, is_dst=is_dst)
        soup_almuten = fetch_almuten_soup(post_data)

        dump_load_http_result(filename=filename_almuten, soup_obj=soup_almuten, is_load_mode=False)
        logger.info(f'走Http请求获取「宫神星」排盘信息，并且 Dump BeautifulSoup to File:{filename_almuten}')

    return soup_ixingpan, soup_almuten


def load_file():
    global name, birthday, location, cur_loc, glon_deg, glat_deg, toffset, is_dst, dist

    name, birthday, location, cur_loc, glon_deg, glat_deg, toffset, is_dst, _ = load_customer_info(customer_name=customer_name)
    load_knowledge_file()
    load_knowledge_data_old()
    load_jobs_file()

    # 从爱星盘字典获取dist
    # dist = load_ixingpan_area(user_input=location)
    # exit(0)


if __name__ == '__main__':
    # --------------- logger 创建文件处理器、创建控制台处理器
    file_handler = logging.FileHandler(f'./out/progression_{customer_name}.log')
    console_handler = logging.StreamHandler()

    # 创建日志格式
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)

    # 将文件处理器添加到日志记录器
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    # ----------------- End logger ---------------

    load_file()

    soup_ixingpan, soup_almuten = get_soup_from_http()

    debug_msg = f'姓名:{name} \n位置信息:{location} \n出生信息:{birthday} \n经纬度信息:{glon_deg} {glat_deg} \n时区:{toffset} \n是否夏令时:{is_dst} \ndist:{dist}\n'
    # print(debug_msg)
    # logger.debug(debug_msg)

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

    # -------------------------- 日返盘 -----------------------------
    get_solar_return()

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
