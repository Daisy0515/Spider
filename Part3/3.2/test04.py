#构造多个参数的请求
from urllib import request,parse
url = 'http://httpbin.org/post'

headers = {
    'User-Agent':'Mozilla/4.0 (compatible; MSIE S. S; Windows NT)',
    'Host':'httpbin.org'
}
dict = {
    'name':'Germey'
}
data = bytes(parse.urlencode(dict),encoding='utf8')
req = request.Request(url,data,headers,method='POST')
response = request.urlopen(req)
print(response.read().decode('utf-8'))