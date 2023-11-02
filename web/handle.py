# coding=utf-8


"""
File: handle.py
Date: 2023/11/01 12:11:35
Brief: 
"""
from typing import Tuple
import hashlib
import reply
import receive
import web
import sys
import cpca


# print("Python版本：", sys.version)

def parse_area(inp_str) -> Tuple[str, str, str]:
    df = cpca.transform([inp_str])

    province = df.iloc[0]['省']
    city = df.iloc[0]['市']
    area = df.iloc[0]['区']
    
    return province, city, area


def get_astro_data(content):
    pass


class Handle(): 
    def POST(self):
        try:
            webData = web.data()
            # print("Handle Post webdata is ", webData)

            recMsg = receive.parse_xml(webData)

            if isinstance(recMsg, receive.Msg) and recMsg.MsgType == 'text':
                toUser = recMsg.FromUserName
                fromUser = recMsg.ToUserName

                content = recMsg.Content
                content = content.decode('utf-8')
                # print(type(content))

                # print(f'content:{content}')
                province, city, area = parse_area(content)

                reply_str = f'省份: {province}\n城市: {city}\n区: {area}'

                replyMsg = reply.TextMsg(toUser, fromUser, reply_str)

                return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"
        except Exception as Argument:
            print(Argument)
            return Argument



