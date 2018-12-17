#cookies
import http.cookiejar,urllib.request
'''
cookie = http.cookiejar.CookieJar() #声明一个CookieJar对象
handler = urllib.request.HTTPCookieProcessor(cookie)#利用HTTPCookieProcessor构建一个Handler
opener = urllib.request.build_opener(handler)#利用build_opener()方法构建出Opener
response = opener.open('http://www.baidu.com')
for item in cookie:
    print(item.name+"="+item.value)
'''
#将cookie传入文件中
filename = 'cookies.txt'
cookie = http.cookiejar.LWPCookieJar(filename)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open('http://www.baidu.com')
cookie.save(ignore_discard=True,ignore_expires=True)

