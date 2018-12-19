#查找节点
#父节点
from pyquery import PyQuery as pq
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
doc =pq(html)
items = doc('.list')
container = items.parent()
print(type(container))
print(container)
#parent()是直接父节点，parents()是祖先节点
print('----------------------------')
parents = items.parents()
print(type(parents))
print(parents)
#输出结果有两个：一个是class为wrap的节点，一个是id为container的节点
#如果想要筛选某个祖先节点的话，可以传入CSS选择器
print('------------------------------')
parent = items.parents('.wrap')
print(parent)