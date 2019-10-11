import requests

url = "https://img-blog.csdnimg.cn/20190927163801418.png"

url_list = [
    "http://e.hiphotos.baidu.com/image/h%3D300/sign=a9e671b9a551f3dedcb2bf64a4eff0ec/4610b912c8fcc3cef70d70409845d688d53f20f7.jpg",
    "http://b.hiphotos.baidu.com/image/h%3D300/sign=92afee66fd36afc3110c39658318eb85/908fa0ec08fa513db777cf78376d55fbb3fbd9b3.jpg",
]

def get_pic(url,n):
    res = requests.get(url)
    c = res.content
    with open(n,"wb") as f:
        f.write(c)

def get_many_pic():
    for url in url_list:
        # 列表.index(成员)
        import time
        time.sleep(0.001)
        # 构建文件名
        n = str(int(time.time()))+".png"
        print(n)
        get_pic(url,n)

get_many_pic()