# 导入一个类
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 获得一个加密器对象
# 加密器 = 类名（盐，过期时间）
obj = Serializer("dragonball", 600)

# 对数据加密
data = {"confirm": 18}
mi = obj.dumps(data)
print('密文创建好了，内容是', mi)
print("http://127.0.0.1:8000/user/active/{}/".format(mi.decode()))

