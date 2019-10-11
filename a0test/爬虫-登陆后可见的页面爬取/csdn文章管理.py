import requests

# 需要的数据
str_cookies = """cookie: uuid_tt_dd=10_28743412270-1569723942844-420746; dc_session_id=10_1569723942844.879679; UserName=ifubing; UserInfo=e72ddbe6095f4d70b8d33a74c9083818; UserToken=e72ddbe6095f4d70b8d33a74c9083818; UserNick=ifubing; AU=94D; UN=ifubing; BT=1569723985205; p_uid=U000000; notice=1; Hm_ct_6bcd52f51e9b3dce32bec4a3997715ac=5744*1*ifubing!6525*1*10_28743412270-1569723942844-420746!1788*1*PC_VC; smidV2=20191005134300f5230bb3cc5b208784317f4b583725d400ed78b71e2634350; aliyun_webUmidToken=T0E516205D4129D3EC233C6038E6A436F9D6858BCC3C1A47F51F930CCB6; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1570254184,1570254379,1570262953,1570263365; TINGYUN_DATA=%7B%22id%22%3A%22-sf2Cni530g%23HL5wvli0FZI%22%2C%22n%22%3A%22WebAction%2FCI%2Fmdeditor%22%2C%22tid%22%3A%22fd405a8b6c0f54%22%2C%22q%22%3A0%2C%22a%22%3A79%7D; dc_tos=pywf5w; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1570273988"""
str_user_agent = """user-agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"""

from spider_tools import parse_header

cookies_dict = parse_header(str_cookies)
cookies = {item.split("=")[0].strip(): item.split("=")[1].strip() for item in cookies_dict['cookie'].strip().split(';')}

print(cookies)
user_agent = parse_header(str_user_agent)

# 请求头
headers = {}
# headers.update(cookies)
headers.update(user_agent)
print(headers)
# 请求网址
url = "https://mp.csdn.net"
# 发起请求
# res = requests.get(url, headers=headers)
res = requests.get(url, headers=headers, cookies= cookies)
# 获取响应
con = res.content.decode()
# 查找是否有草稿箱
idx = con.find("草稿箱")
print(idx)
