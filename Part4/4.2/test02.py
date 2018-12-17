#这个是一个HTML字符串，但是它并不是一个完整的HTML字符串
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
#，该对象的第二个参数为解析器的类型（这里使用lxml），此时就完成了BeaufulSoup 对象的初始化。
#然后，将这个对象赋值给soup 变量。

soup = BeautifulSoup(html,'lxml')
#调用prettify()方法。这个方法可以把要解析的字符串以标准的缩进格式输出。
print(soup.prettify())
#，soup.title
#可以选出HTML中的title节点，再调用string属性就可以得到里面的文本了
print(soup.title.string)
