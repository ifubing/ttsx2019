import requests
import spider_tools

# url = 'http://fanyi.so.com/index/search?eng=1&validate=&query=python'
url = 'http://fanyi.so.com/index/search'
# url = 'http://fanyi.so.com/index/search?eng=0&validate=&query=%E5%8F%AF%E4%BB%A5'
# url = 'http://www.baidu.com'

ua = """User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1
"""
d_ua = spider_tools.parse_header(ua)
print(d_ua)

# postdata= """eng=1&validate=&query=python"""
postdict = {"eng": "1", "validate": "", "query": "happy"}

res = requests.post(url, headers=d_ua, params=postdict)
print(res)
# print()
c = res.content.decode("utf8")

print(type(c), c)

import json

d = json.loads(c)
print(type(d), d)
res = d['data']['explain']['translation']

for i in res:
    print(i)
# with open('a.json', "w", encoding="utf8") as f:
#     f.write()

print('ok')
