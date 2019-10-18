import redis
# redis://121.40.207.159:6379/9
conn = redis.StrictRedis(host="121.40.207.159", port=6379,db=9)
keys = conn.keys()
print(keys)
print(conn)

conn.lrange()
# res = conn.lpush('ltest',1,13,6)
res = conn.lrange('ltest',0,-1)
for r in res:
    print(r)
    print(type(r))
print(res)
