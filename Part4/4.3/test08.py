#获取信息 获取文本
#获取节点之后的另一个主要操作就是获取其内部的文本了，此时可以调用text （）方法来实现：
html='''
<div class="wrap">
<div id="container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
a = doc('.item-0.active a')
print(a)
print(a.text()) #此时它会忽略掉节点内部包含的所有HTML ，只返回纯文字内容。
#如果想要获取这个节点内部的HTML 文本，就要用html()方法了:
print('------------------------')
li = doc('.item-0.active')
print(li)
print(li.html())

#?如果text（）或HTML（）会返回什么内容
print('---------------------------')
lis = doc('li')
print(lis.html())
print(lis.text())
print(type(lis.text()))

