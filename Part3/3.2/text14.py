#quote()该方法可以将内容转化为URL 编码的格式。
#URL 中带有中文参数时，有时可能会导致乱码的问题，此时用这个方法可以将巾文字符转化为URL 编码
from urllib.parse import quote
from urllib.parse import unquote
'''
keyword = '壁纸'
url = 'https://www.baidu.com/s?wd='+quote(keyword)
print(url)
'''
#unquote()进行url解码
url = 'https://www.baidu.com/s?wd=%E5%A3%81%E7%BA%B8'
print(unquote(url))