import redis

sr = redis.StrictRedis(host="121.40.207.159", port=6379, db=0)

# sr =StrictRedis(host="192.168.114.128", port=6379, db=0)

print(sr)
# 添加一个string的键值对
res = sr.set("name", "pyhui1011")
print(res)


