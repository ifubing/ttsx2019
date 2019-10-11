import requests
import random

# 请求网址
def parse_url(url):
    """ 解析网页 """
    res = requests.get(url)
    content = res.content
    # return content

def get_img_url(html):
    """从html中获取图片链接"""
    import re
    img_list = re.findall(r'<img src="(.*?)"', html)
    print(img_list)
    # return img_list

def save_img(img_content):
    # 生成文件名
    n = random.randint(1,1000)
    file_name = str(n)+".jpg"
    # 保存文件
    with open(file_name, "wb") as f:
        f.write(img_content)

def run():
    import time
    url = "https://3w.huanqiu.com/a/667415/9CaKrnQhWV6?agt=8"
    html = parse_url(url)
    print(html)

    # img_list = get_img_url(html.decode())  # [url1, url2]


    for img in None:
    for img in get_img_url(html.decode()):
        print(img)
        img_content = parse_url(img)
        save_img(img_content) # 保存文件

run()