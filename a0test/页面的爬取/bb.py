f = open("111.html", "r", encoding="utf8")
con = f.read()
f.close()

print(con)

import re

# res = re.findall("<h4 class=""(.*?)</h4>", con, re.DOTALL)
res = re.findall("<h4 .*? (.*?)</h4>", con, re.DOTALL)
print(res)


for r in res:
    print(r)
    print('.....')



"""
<h4 class="">
        <a href="https://blog.csdn.net/ifubing/article/details/101427344" target="_blank">
        <span class="article-type type-1 float-none">原创</span>        爬虫-01-基础入门-字符串基础知识-节符串与字节转换      </a>
    </h4>
"""
