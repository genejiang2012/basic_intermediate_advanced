

import requests
from urllib import request
from urllib import parse
from http import cookiejar

# 声明一个CookieJar对象实例来保存cookie
cookie = cookiejar.CookieJar()
# 利用urllib库中的request的HTTPCookieProcessor对象来创建cookie处理器
handler = request.HTTPCookieProcessor(cookie)
# 通过handler来构建opener
opener = request.build_opener(handler)
# 此处的open方法同urllib的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
print(cookie)
for item in cookie:
    print('Name = '+item.name)
    print('Value = '+item.value)
