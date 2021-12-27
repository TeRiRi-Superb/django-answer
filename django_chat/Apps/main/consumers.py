from channels.generic.websocket import WebsocketConsumer
from channels.exceptions import StopConsumer
from .models import Answer, HighProblem
import requests
import datetime
from urllib import parse


class ChatConsumer(WebsocketConsumer):
    def websocket_connect(self, message):
        # 客户端发送建立连接请求
        # 建立连接
        print('建立连接')
        self.accept()

    def websocket_receive(self, message):
        # 接受客户端的消息
        print(message)
        # 按天记录高频短语
        try:
            year = datetime.datetime.now().year
            month = datetime.datetime.now().month
            day = datetime.datetime.now().day
            print(year, day)

            problem = HighProblem.objects.get(problem=message['text'], ask_time__day=day, ask_time__month=month, ask_time__year=year)

            problem.count += 1
            problem.save()
        except Exception as e:
            HighProblem.objects.create(problem=message['text'], count=1)

        # 是否已经录入应答库，未录入调用应答api
        try:
            text = Answer.objects.get(problem=message['text']).solutions
        except:
            data = {}
            data["appkey"] = "cc242dfd6026a245"
            data["question"] = message['text']

            url_values = parse.urlencode(data)
            url = "https://api.binstd.com/iqa/query" + "?" + url_values

            result = requests.get(url)
            jsonarr = result.json()
            text = jsonarr['result']['content']
            if text == 'defaultReply':
                text = '无法回答这个问题'

        # 向客户端发送
        self.send(text)


    def websocket_disconnect(self, message):
        # 断开连接
        raise StopConsumer()