#urlparse()
#该方法可以实现URL 的识别和分段：

from urllib.parse import urlparse
url = 'http://www.baidu.com/index.html;user?id=S#comment'
'''
result = urlparse(url)
print(type(result),'\n',result)
'''
#测试allow_fragments参数
#如果它被设置为false，fragment部分就会被忽略，它会被解析为path，parameters或者query的一部分，而fragment部分为空
result = urlparse(url=url,allow_fragments=False)
print(result)

#假设URL中不包含params和query
url1='http://www.baidu.com/index.html#comment'
result = urlparse(url=url1,allow_fragments=False)
print(result.scheme,result[0],result.netloc,result[1])



