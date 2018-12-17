import requests
'''
r = requests.get('https://www.baidu.com/')
print(type(r))
print(r.status_code)
print(type(r.text))
print(r.text)
print(r.cookies)
'''
data={
    'name':'germey',
    'age':22
}
r = requests.get("http://httpbin.org/get",params=data)
print(type(r.text))
print(r.json())
print(type(r.json()))
