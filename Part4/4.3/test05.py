#兄弟节点
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
doc = pq(html)
#选择class为list的节点内部class为item-0和active的节点
li = doc('.list .item-0.active')
print(li.siblings())
print('--------------')
print(li.siblings('.active'))
