from lxml import etree
text = '''
<div>
<ul>
<li class="item-O"><a href="link1.html">first item</a><li>
<li class="item-1"><a href="link2.html">second item</a><li>
<li class="item-inactive"><a href="link3.html”>third item</a></li>
<li class="item-1"><a href="link4.html">fourth item</a></li>
<li class="item-0"><a href＝"link5.html">fifth item</a>
</ul>
</div>
'''
html = etree.HTML(text)#调用HTML类进行初始化，这样就成功构造了一个XPath解析对象
result = etree.tostring(html) #调用tostring()方法可输出修正后的HTML代码，但是结果是bytes类型
print(result.decode('utf-8'))#利用decode()将其转成str类型

'''
#也可以直接读取文本进行解析
html1 = etree.parse('./test.html',etree.HTMLParser())
result = etree.tostring(html1)
print(result.decode('utf-8'))
'''

