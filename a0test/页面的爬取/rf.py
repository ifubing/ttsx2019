f = open("ifubing.html", "r", encoding="utf8")
c = f.read()
print(c)

import re
# 当前页的全部文章列表
url_list = re.findall(r'<h3><a href="(.*?)" target="_blank" class="sub_title">', c)
# 当前页的标题
title = re.findall(r'<title>(.*?)</title>', c)
print(title)


res = re.findall(r"<h3>(.*?)</h3>", c, re.DOTALL)
print(res)

d = {}
for i in res:
    # print(i)
    li = i.split()
    print(li)
    url = li[1].lstrip('href=').strip('"')
    name = li[-1].strip('</a>')

    d[name] = url

print(d)


for k,v in d.items():
    print('标题是{}'.format(k))
    print('链接是{}'.format(v))
    print("*"*10)