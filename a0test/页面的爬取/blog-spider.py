import requests

url = "https://me.csdn.net/ifubing"

# https://blog.csdn.net/ifubing
# https://blog.csdn.net/ifubing/article/list/2?

res = requests.get(url)

con = res.content.decode()

print(con)

with open("ifubing.html", "w", encoding="utf8") as f:
    f.write(con)