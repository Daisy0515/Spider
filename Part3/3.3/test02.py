import re

content = 'Hello 1234567 World_This is a Regex Demo'
'''
result = re.match('^Hello\s(\d+)\sWorld',content)
'''
#贪婪与非贪婪
result = re.match('^He.*?(\d+).*Demo$',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())