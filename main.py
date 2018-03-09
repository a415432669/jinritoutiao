import requests
from config import *
import json
import re

def get_index_page(offset,keyword):
    data = "offset=0&format=json&keyword=%s&autoload=true&count=20&cur_tab=1&from=search_tab"%keyword
    base = 'https://www.toutiao.com/search_content/?'
    #print(data)
    try:
       res = requests.get(base+data)
       if res.status_code == 200:
           return res.text
       return None
    except Exception:
        print('请求错误')
        print(Exception)
        return None

def parse_index_page(text):
    try:
        dictText = json.loads(text)
        #list = dictText.data
        print(dictText)
        if dictText and 'data' in dictText.keys():
            for item in dictText.get('data'):
                #print(item.get('article_url'))
                yield item.get('article_url')
    except Exception:
        print('parse_index_page')
        pass


def get_page_content(url):
        print(url)
        header = {
            'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.104 Safari/537.36 Core/1.53.4620.400 QQBrowser/9.7.13014.400'
        }
        res = requests.get(url,headers=header)
        if res.status_code == 200:
            text = res.text
            print(text)
            imagePattern = re.compile('var BASE_DATA = (.*?);</script>',re.S)
            result = re.search(imagePattern,text)
            print(result)
            dict = json.loads(result)
            #print(dict['articleInfo']['title'])
            return dict['articleInfo']['title']


    # except Exception:
    #     print(Exception)
    #     return None



if __name__ == '__main__':
    text = get_index_page(0,KEYWORD)
    pageList = parse_index_page(text)
    for item in pageList:
        print(get_page_content(item))

