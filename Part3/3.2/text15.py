import urllib
from urllib.robotparser import RobotFileParser
'''
rp = RobotFileParser()
rp.set_url('http://www.jianshu.com/robots.txt')
rp.read()
print(rp.can_fetch('*','http://www.jianshu.com/p/67554025d7d'))
print(rp.can_fetch('*',"http://www.jianshu.com/search?q=python&page=l&type=collections"))

'''
from urllib.request import urlopen
'''
403异常：
之所以出现上面的异常,是因为如果用 urllib.request.urlopen 方式打开一个URL,
服务器端只会收到一个单纯的对于该页面访问的请求,
但是服务器并不知道发送这个请求使用的浏览器,操作系统,硬件平台等信息,
而缺失这些信息的请求往往都是非正常的访问,例如爬虫.
在请求中加入UserAgent的信息
'''
rp = RobotFileParser()
url = 'http://www.jianshu.com/robots.txt'
headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)'
}
req = urllib.request.Request(url=url, headers=headers)
rp.parse(urlopen(req).read().decode('utf-8').split('\n'))
print(rp.can_fetch('*','http://www.jianshu.com/p/67554025d7d'))
print(rp.can_fetch('*',"http://www.jianshu.com/search?q=python&page=l&type=collections"))