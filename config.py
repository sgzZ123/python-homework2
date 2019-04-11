url = 'http://data.stats.gov.cn/easyquery.htm'
popularity = '[{"wdcode":"zb","valuecode":"A0301"}]'
agestructure = '[{"wdcode":"zb","valuecode":"A0303"}]'


# 返回相应的参数值
def SearchContent(content):
    if type(content) == str:
        if content == 'popularity':
            return popularity
        elif content == 'agestructure':
            return agestructure
    elif type(content) == int:
        return '[{"wdcode":"sj","valuecode":"%d"}]' % (content,)

