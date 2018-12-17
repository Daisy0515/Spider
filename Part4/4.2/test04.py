#提取信息
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
#获取名称,可以利用name 属性获取节点的名称
print(soup.title.name)
#获取属性，调用attrs获取所有属性：
print(soup.p.attrs)
print(soup.p.attrs['name'])
print(soup.p['name'])
print(soup.p['class'])

#嵌套选择
#每一个返回结果都是bs4.element.Tag类型,
#它同样可以继续调用节点进行下一步的选择
html1='''
<html><head><title>the Dormouse's story</title></head>
<body>
'''
soup1 = BeautifulSoup(html1,'lxml')
print(soup1.head.title)
print(type(soup1.head.title))
print(soup1.head.title.string)

#关联选择
#子节点和子孙节点
print(soup.p.contents)

