from urllib import request,error
url = 'https://cuiqingcai.com/index.htm'
'''
try:
    response = request.urlopen(url)
except error.URLError as e:
    print('错误原因',e.reason)

'''
'''
try:
    response = request.urlopen(url)
    print(response.read().decode('utf-8'))
except error.HTTPError as e:
    print(e.reason,e.code,e.headers,seq='\n')
'''
try:
    response = request.urlopen(url)
except error.HTTPError as e:
    print(e.reason, e.code, e.headers, seq='\n')
except error.URLError as e:
    print('错误原因',e.reason)
else:
    print('Request Successfully')
