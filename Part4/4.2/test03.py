#节点选择器
#直接调用节点的名称就可以选择节点元素，再调用string 属性就可以得到节点内的文本了
html = '''
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse"><b> The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="linkl"><!--Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2"> Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well .</p>
<p class="story"> ... </p>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.title)
print(type(soup.title))
print(soup.title.string)
print(soup.head)
print(soup.p)#当有多个节点时，这种选择方式只会选择到第一个匹配的节点，其他的后面节点都会忽略