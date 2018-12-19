#remove()
#remove()方法就是移除，它有时会为信息的提取带来非常大的便利。
html = '''
<div class="wrap">
hello,world
<p>This is a paragraph.</p>
</div>
'''
from pyquery import PyQuery as pq
doc = pq(html)
wrap=doc('.wrap')
print(wrap.text())
#现在想提取Hello, World 这个字符串，而不要p节点内部的字符串
wrap.find('p').remove()
print(wrap.text())
