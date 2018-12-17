from lxml import etree
text = '''
<div>
<ul>
<li class="item-0"><a href="link1.html">first item</a></li>
<li class="item-1"><a href="link2.html">second item</a></li>
<li class="item-inactive"><a href="link3.html">third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href="link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)#调用HTML类进行初始化，这样就成功构造了一个XPath解析对象
result0 = etree.tostring(html) #调用tostring()方法可输出修正后的HTML代码，但是结果是bytes类型
print(result0.decode('utf-8'))#利用decode()将其转成str类型
result = html.xpath('//*') #我们一般会用刀开头的XPath 规则来选取所有符合要求的节点
print(result)
#*代表匹配所有节点，整个HTML中的所有节点都会被获取

#也可指定节点名称
result1 = html.xpath('//li')
print(result1)
print(result1[0])

#寻找子节点
result2 = html.xpath('//li/a')
print(result2)

#/用于选取直接子节点，如果要获取所有子孙节点，就可以使用//
result3 = html.xpath('//ul//a')
print(result3)

#父节点
#首先选中href 属性为link4.html的a节点，然后再获取其父节点，然后再获取其class属性
result4 = html.xpath('//a[@href="link4.html"]/../@class')
print(result4)
#同时，我们也可以通过parent::来获取父节点，代码如下
result5 = html.xpath('//a[@href="link3.html"]/parent::*/@class')
print(result5)
#属性匹配
#我们还可以用@符号进行属性过滤。比如，这里如果要选取class为item-1的li节点
result6 = html.xpath('//li[@class="item-0"]')
print(result6)

#文本获取
#text（）方法获取节点中的文本，接下来尝试获取前面li节点中的文本
result7 = html.xpath('//li[@class="item-0"]/a/text()')
print(result7)
result8 = html.xpath('//li[@class="item-0"]//text()')
print(result8)

#属性获取
#获取所有li节点下所有a节点的href属性
result9 = html.xpath('//li/a/@href')
print(result9)

#属性多值匹配
#有时候，某些节点的某个属性可能有多个值
text1 = '''
<li class="li li-first"><a href="link.html">first item</a></li>
'''
html1 = etree.HTML(text1)
result10 = html1.xpath('//li[@class="li"]/a/text()')
#li 节点的class 属性有两个值li 和li-first ，此时如果还想用之前的属性民配获取，就无法匹配了
print(result10)
result11 = html1.xpath('//li[contains(@class,"li")]/a/text()')
print(result11)

#多属性匹配
#我们可能还遇到一种情况，那就是根据多个属性确定一个节点，这时就需要同时匹配多个属性。此时可以使用运算符and来连接
text2 = '''
<li class="li li-first" name="item"><a href="link.html">first item</a></li>
'''
html2 = etree.HTML(text2)
result12 = html2.xpath('//li[contains(@class,"li") and @name = "item"]/a/text()')
print(result12)