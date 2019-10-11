import redis

conn = redis.StrictRedis(host="192.168.114.130", port=6379, db=0)
print(conn)
conn.set("age", "18")
print('ok')


import djan