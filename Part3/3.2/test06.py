#代理
from urllib.error import URLError
from urllib.request import ProxyHandler,build_opener

#设置代理IP
proxy_hander = ProxyHandler({
     'http': '127.0.0.0:4973' #只用设置一种代理IP地址即可
})
opener = build_opener(proxy_hander) #通过proxy_handler来构建opener

try:
    response = opener.open('https://www.baidu.com')
    html = response.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)