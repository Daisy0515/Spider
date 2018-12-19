#查找节点
#子节点，需要用到find()方法，此时传人的参数是css选择器
from pyquery import PyQuery as pq
html='''
<div id = "container">
<ul class="list">
<li class="item-0">first item</li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
<li class="item-1 active"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a></li>
</ul>
</div>
'''
doc = pq(html)
items = doc('.list')
print(type(items))
print(items)
lis = items.find('li')
print(type(lis))
print(lis)

#其实find()的查找范围是节点的所有子孙节点，如果我们只想查找子节点，那么可以用children（）方法
lis = items.children('.active')
print(type(lis))
print(lis)



