#有时候，reason 属性返回的不一定是字符串，也可能是一个对象
import socket
import urllib.request
from urllib import error
import urllib.error

url = 'https://www.baidu.com'
try:
    response = urllib.request.urlopen(url=url,timeout=0.01)
except error.URLError as e:
    print(type(e.reason))
    if isinstance(e.reason,socket.timeout): #reason 属性的结果是socket.timeout类
        print('TIME OUT')