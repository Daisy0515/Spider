from lxml import etree
#按序选择
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html"><span>first item</span></a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)
'''
result = html.xpath('//li[1]/a/text()')
print(result)
result = html.xpath('//li[last()]/a/text()')
print(result)
result = html.xpath('//li[position()<3]/a/text()')
print(result)
result = html.xpath('//li[last()-2]/a/text()')
print(result)
'''
#节点轴选择
#我们调用了ancestor 轴，可以获取所有祖先节点。其后需要跟两个冒号，然后是节点的选择器，这里我们直接使用＊
result = html.xpath('//li[1]/ancestor::*')
print(result)
result = html.xpath('//li[1]/ancestor::div')
print(result)
#我们调用了attribute 轴，可以获取所有属性值，其后跟的选择器还是＊，这代表
#获取节点的所有属性，返回值就是li 节点的所有属性值。
result = html.xpath('//li[1]/attribute::*')
print(result)
#我们调用了child 轴，可以获取所有直接子节点。这里我们又加了限定条件，选
#取href 属性为linkl.html的a节点
result = html.xpath('//li[1]/child::a[@href="link1.html"]')
print(result)
#我们调用了descendant 轴，可以获取所有子孙节点。这里我们又加了限定条件获
#取span 节点，所以返回的结果只包含span节点而不包含a节点
result = html.xpath('//li[1]/descendant::span')
print(result)
#我们调用了following 轴，可以获取当前节点之后的所有节点。这里我们虽然使
#用的是＊匹配，但又加了索引选择，所以只获取了第二个后续节点。
result = html.xpath('//li[1]/following::*[2]') #???
print(result)
#我们调用了following -s ibling 轴，可以获取当前节点之后的所有同级节点
result = html.xpath('//li[1]/following-sibling::*')
print(result)


