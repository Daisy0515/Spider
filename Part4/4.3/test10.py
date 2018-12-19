#除了操作class这个属性外，也可以用attr()方法对属性进行操作。此外，还可以用text()
#和html()方法来改变节点内部的内容。
html='''
<ul class = "list">
<li class = "item-0 active"><a href="link3.html"><span class="bold">third item</span></a></li>
</ul>
'''
from pyquery import PyQuery as pq
doc = pq(html)
li = doc('.item-0.active')
print(li)
#调用attr()方法后，li节点多了一个原本不存在的属性name,其值为link
li.attr('name','link')
print(li)

#调用text()方法，传入文本之后，li节点内部的文本全被改为传入的字符串文本了。
li.text('changed item')
print(li)

#调用html()方法传人HTML 文本后li 节点内部又变为传人的HTML 文本了
li.html('<span>changed item</span>')
print(li)