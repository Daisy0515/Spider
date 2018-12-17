import urllib.request

response = urllib.request.urlopen('https://www.python.org')
#print(response.read().decode('utf-8'))

#利用type()放大输出响应的类型：
#print(type(response))

print(response.status)
print(response.getheaders())
print(response.getheader('Server'))
