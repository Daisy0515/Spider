'''
#urljoin()
from urllib.parse import urljoin
print(urljoin('http://www.baidu.com','FAQ.html'))
print(urljoin('http://www .baidu.com','https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html'))
print(urljoin('http://www.baidu.com/about.html','https://cuiqingcai.com/FAQ.html?question=2'))
print(urljoin('http://www.baidu.com?wd=abc','https://cuiqingcai.com/index.php'))
print(urljoin('http://www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com','?category=2#comment'))
print(urljoin('www.baidu.com#comment','?category=2'))
'''
#urlencode()
'''
from urllib.parse import urlencode
params = {
    'name':'germey',
    'age':22
}
base_url = 'http://www.baidu,com?'
url = base_url+urlencode(params)
#参数就成功地由字典类型转化为GET 请求参数了。
print(url)
'''
#parse_qs()有了序列化，必然就有反序列化
#parse_qsl()方法，它用于将参数转化为元组组成的列表
from  urllib.parse import parse_qs

query = 'name=germey&age=22'
print(parse_qs(query))
