#方法选择器
#find_all  find_a ll(narne , attrs , recursive , text , **kwargs)
html='''
<div class="panel">
<div class="panel-heading">
<h4>Hello</h4>
</div>
<div class="panel-body">
<ul class="list" id="list-1" name="elements">
<li class="element">Foo</li>
<li class="element">Bar</li>
<li class="elernent">Jay</li>
</ul>
<ul class="list list-small" id ＝"list-2 ">
<li class="element">Foo</li>
<li class="element">Bar</li>
</ul>
</div>
</div>
'''
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'lxml')
print(soup.prettify())
#name
print(soup.find_all(name='ul'))
print(type(soup.find_all(name='ul')[0]))
#attrs,传入属性来查询
print(soup.find_all(attrs={'id':'list-1'}))
print(soup.find_all(attrs={'name':'elements'}))
'''
#text,匹配节点的文本，传入的形式可以是字符串，也可以是正则表达式
import re
from bs4 import BeautifulSoup
html1='''
<div class="panel">
<div class="panel-body">
<a>Hello,this is a link</a>
<a>Hello,this is a link,too</a>
</div>
</div>
'''
soup1 = BeautifulSoup(html1,'lxml')
print(soup1.find_all(text=re.compile('link')))