from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from django.contrib import auth
from celery_tasks.tasks import one

from django.contrib import auth
def test(request):

    user = request.user
    print('user，登陆状态时')
    print(user)

    auth.logout(request)
    user = request.user
    print('user，退出登陆以后')
    print(user)

    print('user is authentic')
    print(user.is_authenticated)

    return render(request,"test.html")


def testfather(request):
    return render(request,"testbase.html")


def testson(request):
    return render(request,"testson.html")

