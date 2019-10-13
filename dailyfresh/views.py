from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from django.contrib import auth
from celery_tasks.tasks import one

from django.contrib import auth
def test(request):
    import redis
    # redis://121.40.207.159:6379/9
    conn = redis.StrictRedis(host="121.40.207.159", port=6379, db=9)
    keys = conn.keys()
    print(keys)
    print(conn)

    import django_redis
    conn = django_redis.get_redis_connection('default')
    print(conn)

    return render(request,"test.html")


def testfather(request):
    return render(request,"testbase.html")


def testson(request):
    return render(request,"testson.html")

