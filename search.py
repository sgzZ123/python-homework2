import requests
import time
import json
from config import *


# 爬虫类
class scraper:
    def __init__(self):
        # 建立会话和头部、参数
        self.session = requests.session()
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        self.keys = {'m': 'QueryData', 'dbcode': 'hgnd', 'rowcode': 'zb', 'colcode': 'sj', 'wds': '[]', 'dfwds': '[]',
                     'k1': str(int(round(time.time() * 1000)))} 

    # 从网页获取信息
    def GetInfomation(self, content, years):
        session = requests.session()
        # 异常判断
        if not years or not content or type(content) != str:
            raise TypeError
        result = []

        # 调整参数，发起请求，查询这一类数据
        self.keys['dfwds'] = SearchContent(content)
        reply = session.post(url, params=self.keys, headers=self.header)
        if reply.status_code != 200:
            return -1

        # 查询各年数据
        try:
            for year in years:
                self.keys['dfwds'] = SearchContent(year)
                reply = session.post(url, params=self.keys, headers=self.header)
                while True:
                    try:
                        js    = json.loads(reply.text)
                        break
                    except:
                        print('network error')
                        print(reply.text)
                        time.sleep(0.5)
                        session = requests.session()
                        self.keys['dfwds'] = SearchContent(content)
                        reply = session.post(url, params=self.keys, headers=self.header)
                        self.keys['dfwds'] = SearchContent(year)
                        reply = session.post(url, params=self.keys, headers=self.header)
                KeyInfo = js['returndata']
                data_dict_list = KeyInfo['datanodes']
                description_dict_list = KeyInfo['wdnodes'][0]['nodes']
                result_dict = {'year':str(year)}
                for i in range(len(data_dict_list)):
                    result_dict[ description_dict_list[i]['name'] ] = data_dict_list[i]['data']['strdata']
                    result_dict['unit'] = description_dict_list[i]['unit']
                result.append(result_dict)
        except TypeError:
            return

        return result
