#compile()这个方法可以将正则字符串编译成正则表达式对象，以便在后面的匹配中复用。
import re
content1 = '2016-12-15 12:00'
content2 = '2016-12-17 11:00'
content3 = '2016-12-22 13:00'
pattern = re.compile('\d{2}:\d{2}')
result1 = re.sub(pattern,'',content1)
result2 = re.sub(pattern,'',content2)
result3 = re.sub(pattern,'',content3)
print(result1,result2,result3)

