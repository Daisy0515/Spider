
import requests
'''
#post请求
data = {'name':'germey','age':'22'}
r = requests.post("http://httpbin.org/post",data=data)
print(r.text)
'''
'''
#响应
url='http://www.jianshu.com'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r = requests.get(url=url,headers=headers)
print(type(r.status_code),r.status_code)
print(type(r.headers),r.headers)
print(type(r.cookies),r.cookies)
print(type(r.url),r.url)
print(type(r.history),r.history)
'''
#状态码常用来判断请求是否成功，而requests 还提供了一个内置的状态码查询对象requests.codes
import requests
url='http://www.jianshu.com'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r = requests.get(url=url,headers=headers)
exit() if not r.status_code == requests.codes.ok else print('Request Successfully')
#这里通过比较返回码和内置的成功的返回码，来保证请求得到了正常响应，输出成功请求的消息，
#否则程序终止，这里我们用requests.codes .ok 得到的是成功的状态码200。
