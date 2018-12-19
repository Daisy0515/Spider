#获取信息 获取属性
#提取到某个PyQuery 类型的节点后，就可以调用attr （）方法来获取属性：
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
#选中class为item-0和active的li节点内的a节点
a = doc('.item-0.active a')
print(a,type(a))
print(a.attr('href')) #print(a.attr.href)

a = doc('a') #
print(a,type(a))
print(a.attr('href'))
# 这是因为，当返回结果包含多个节点时，调用attr （）方法，只会得
# 到第一个节点的属性。
print(a.attr.href)

for item in a.items():
    print(item.attr('href'))