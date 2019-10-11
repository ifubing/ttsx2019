import redis

conn = redis.StrictRedis(host="121.40.207.159", port=6379, db=0)
print(conn)

conn.set('name','zs')
print('ok')