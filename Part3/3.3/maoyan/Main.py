import requests
import re
import json
import time
from requests.exceptions import RequestException

def get_one_page(url):
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
        }
        response = requests.get(url,headers=headers)
        if response.status_code == 200:
            return response.text
        return None
    except RequestException:
        return None

def parse_one_page(html):
    pattern = re.compile(
        '<dd>.*?board-index.*?>(.*?)</i>.*?data-src="(.*?)".*?name.*?a.*?>(.*?)</a>.*?star.*?>(.*?)</p>.*?releasetime.*?>'
        '(.*?)</p>.*?integer.*?>(.*?)</i>.*?fraction.*?>(.*?)</i>.*?</dd>',
        re.S
    )
    items = re.findall(pattern,html)
    for item in items:
        yield {
            'index':item[0],
            'image':item[1],
            'title':item[2].strip(),
            'actor':item[3].strip()[3:] ,
            'time': item[4].strip()[5:] ,
            'score': item[5]+item[6]

        }
    '''
    for item in items:
            print('index:',item[0])
            print('image:',item[1])
            print('title:',item[2].strip())
            print('actor:',item[3].strip()[3:] if len(item[3]) > 3 else '')
            print('time:',item[4].strip()[5:] if len(item[4]) > 5 else '')
            print('score:',item[5].strip() + item[6].strip())
    '''
#写入文件
#这里通过JSON 库的dumps()方法实现字典的序列化，
#并指定ensure ascii 参数为False ，这样可以保证输出结果是中文形式而不是Unicode 编码
def write_to_file(content):
    with open('result.txt','a',encoding='utf-8') as f:
        f.write(json.dumps(content,ensure_ascii=False)+'\n')

def main(offset):
    url = 'https://maoyan.com/board/4?offset=' + str(offset)
    html = get_one_page(url)
    for item in parse_one_page(html):
        print(item)
        write_to_file(item)

if __name__ == '__main__':
    for i in range(10):
        main(offset=i*10)
        time.sleep(1)