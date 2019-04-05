import requests
import time
import json
from config import *


class scraper:
    def __init__(self):
        self.session = requests.session()
        self.header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
        self.keys = {'m': 'QueryData', 'dbcode': 'hgnd', 'rowcode': 'zb', 'colcode': 'sj', 'wds': '[]', 'dfwds': '[]',
                     'k1': str(int(round(time.time() * 1000)))}

    def GetInfomation(self, content, years):
        if not years or not content or type(content) != str:
            raise TypeError
        result = []

        self.keys['dfwds'] = SearchContent(content)
        reply = self.session.get(url, params=self.keys, headers=self.header)
        if reply.status_code != 200:
            return

        try:
            for year in years:
                self.keys['dfwds'] = SearchContent(year)
                reply = self.session.get(url, params=self.keys, headers=self.header)
                js    = json.loads(reply.text)
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


