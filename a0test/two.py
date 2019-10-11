import requests

data = """
query: 中国
from: zh
to: en
token: ebe0f0e722d022e3f26d2c1f6606c2ff
sign: 777849.998728
"""

data_line = data.strip().split("\n")
data_dict = {line.split(":")[0].strip(): line.split(":")[1].strip() for line in data_line}
print(data_dict)


url = "https://fanyi.baidu.com/basetrans"
res = requests.post(url, params=data_dict)
print(res.status_code)
print('fanyi', res.content.decode())