#像Beautiful Soup 一样，初始化pyquery 的时候，也需要传入HTML 文本来初始化一个PyQue1y对象。
#字符串初始化
html='''
<div>
<ul>
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
print(doc('li')) #传入li节点，选择所有li节点

#URL初始化
#初始化的参数不仅可以以字符串的形式传递，还可以传入网页的URL
doc = pq(url='https://cuiqingcai.com')
#doc = pq(requests.get('https://cuiqingcai.com').text)
print(doc('title'))

#文件初始化
doc = pq(filename='demo.html')
print(doc('li'))