#HTTPBasicAuthHandler:用于管理认证，
# 如果一个链接打开时需要认证，那么可以用它来解决认证问题
#???实验失败
from urllib.request import HTTPPasswordMgrWithDefaultRealm,HTTPBasicAuthHandler,build_opener
from urllib.error import URLError

username = '15867123809'
password = '123456'
url = 'http://router.intchain.io/#/'

p = HTTPPasswordMgrWithDefaultRealm()
p.add_password(None,url,username,password)
auth_handler = HTTPBasicAuthHandler(p)
opener = build_opener(auth_handler)

try:
    result = opener.open(url)
    html = result.read().decode('utf-8')
    print(html)
except URLError as e:
    print(e.reason)
