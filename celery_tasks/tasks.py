# 导入相关的模块
from django.core.mail import send_mail
from django.conf import settings

# 导入类
from celery import Celery

# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dailyfresh.settings')
# django.setup()

# 创建一个Celery类的实例对象
app = Celery("celery_tasks.tasks", broker="redis://192.168.114.128:6379/8")
# sr =StrictRedis(host="192.168.114.128", port=6379, db=0)
# app = Celery("celery_tasks.tasks", broker="redis://192.168.114.128:6379/8")

@app.task
def one():
    print('start one')
    import time
    time.sleep(20)
    print('end one')


# 定义任务函数
@app.task
def send_register_active_email(to_email, username, token):
    """发送激活邮件"""
    print('*'*10)
    print(to_email, username, token)
    # subject = "天天生鲜欢迎信息"
    # message = ""
    # sender = settings.EMAIL_FROM
    # receiver = [to_email]
    # html_message = '欢迎{0}注册dj鲜生，你的激活链接是<a href="{1}">{1}</a>'.format(username, token)
    # send_mail(subject, message, sender, receiver, html_message=html_message)
