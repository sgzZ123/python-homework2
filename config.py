url = 'http://data.stats.gov.cn/easyquery.htm'
popularity = '[{"wdcode":"zb","valuecode":"A0301"}]'


def SearchContent(content):
    if type(content) == str:
        if content == 'popularity':
            return popularity
    elif type(content) == int:
        return '[{"wdcode":"sj","valuecode":"%d"}]' % (content,)

