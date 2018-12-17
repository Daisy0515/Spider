'''
#urlunparse
from urllib.parse import urlunparse
#长度必须为6
data = ['http','www.baidu.com','index.html','user','a=6','comment']
print(urlunparse(data))
'''
from urllib.parse import urlsplit
url='http://www.baidu.com/index.html;user?id=6#comment'
result = urlsplit(url)
print(result)