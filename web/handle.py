# coding=utf-8


"""
File: handle.py
Date: 2023/11/01 12:11:35
Brief: 
"""

import hashlib
import reply
import receive
import web
import sys

# print("Python版本：", sys.version)

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

                replyMsg = reply.TextMsg(toUser, fromUser, content)

                return replyMsg.send()
            else:
                print("暂且不处理")
                return "success"
        except Exception as Argument:
            print(Argument)
            return Argument



