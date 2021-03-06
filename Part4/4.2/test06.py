#find(),返回的是单个元素，也就是匹配的第一个元素，find_all()匹配的是所有匹配元素组成的列表
html='''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="element">Jay</li>
</ul>
<ul class="list list-small" id="list-2">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div> 
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.find(name='ul'))
print(type(soup.find(name='ul')))
print(soup.find(class_='list'))

#find_parents():返回所有祖先节点
#find_parent():返回直接父亲节点
#find_next_siblings()返回后面所有的兄弟节点
#find_next_sibling()返回后面第一个兄弟节点
#find_previous_siblings()返回前面所有的兄弟节点
#find_previous_sibling()返回前面第一个兄弟节点
#find_all_next():返回节点后所有符合条件的节点
#find_next():返回第一个符合条件的节点
#find_all_previous():返回节点前所有符合条件的节点
#find_previous():后者返回第一个符合条件的节点

