#requests高级用法cookie
import requests
'''
#文件上传

files = {'file':open('favicon.ico','rb')}
r = requests.post("http://httpbin.org/post",files=files)
print(r.text)
'''
'''
#cookies
r = requests.get("https://www.baidu.com")
print(r.cookies)
for key,value in r.cookies.items():
    print(key + '=' + value)
'''
headers = {
    'cookie':'zap=63fd10db-7145-4042-8efc-39d435bc5579; _xsrf=2xIlJarqKqgx4RyPDzpBiaI2fxWh0sOy; d_c0="AAAoCAMtcQ6PTtlTL1jc24Yc_VPtKmxqefI=|1540893269"; z_c0="2|1:0|10:1540893292|4:z_c0|92:Mi4xVEtFbEF3QUFBQUFBb09mNkFpMXhEaVlBQUFCZ0FsVk5iSGpGWEFBRzZJY1FYT1pFWHBpUVVIWnk4WndUQTRkMllB|3dfae79f31dd84d304a44a05c9a4a648314be4b3e19c59c2d9e436a7b25d03dd"; tst=r; q_c1=13027a885a2c48089c546421fe368996|1543713061000|1540893293000; __utmz=51854390.1543713064.1.1.utmcsr=zhihu.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utmv=51854390.100--|2=registration_date=20160615=1^3=entry_date=20160615=1; __utma=51854390.364375764.1543713064.1543713064.1544685439.2; __utmc=51854390; tgw_l7_route=170010e948f1b2a2d4c7f3737c85e98c',
    'Host':'www.zhihu.com',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'
}
r = requests.get('https://www.zhihu.com',headers=headers)
print(r.text)

