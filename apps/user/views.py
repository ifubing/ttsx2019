import re

from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect

from django.urls import reverse

# 用户相关功能
from django.contrib.auth import login, logout

# 导入这是危险的加密器类
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer

# 导入celery任务函数
from celery_tasks.tasks import send_register_active_email

# from apps.user.models import User  当前情况下会报错的导入法
from user.models import User
from user.models import Address

from django.views.generic import View


# Create your views here.


# /user/register
# 类视图
class RegisterView(View):
    """注册"""

    def get(self, request):
        """get请求执行"""
        return render(request, "register.html")

    def post(self, request):
        """post请求执行"""
        print('view,post')
        user_name = request.POST.get("user_name")
        password = request.POST.get("pwd")
        email = request.POST.get("email")
        allow = request.POST.get("allow")
        # 数据校验
        print('user_name', user_name)
        print('password', password)
        print('email', email)

        # 校验：是否有空数据
        if not all([user_name, password, email]):
            print('有不合法的数据空数据进来了')
            return render(request, "register.html",
                          {"errmsg": "数据不完整"})
        # 校验：邮箱格式
        is_mail = re.match(r'^[a-z0-9][\w.\-]*@[a-z0-9\-]+(\.[a-z]{2,5}){1,2}$', email)
        print('ismail', is_mail)
        if not is_mail:
            print('不是邮箱')
            return render(request, "register.html",
                          {"errmsg": "邮箱格式不正确"})
        # 校验：是否有勾选协议
        if allow != "on":
            print('得同意协议')
            return render(request, "register.html",
                          {"errmsg": "请同意协议"})

        # 用户重名的验证 todo 临时有事，回来再补
        try:
            user = User.objects.get(username=user_name)
            print('用户查询结果', user)
        except User.DoesNotExist:
            user = None
            print('查到重名的')

        if user:
            print('用户名已经存在')
            return render(request, "register.html",
                          {"errmsg": "用户名已经存在请更换用户名"})

        # 进行业务处理，即，进行用户注册
        user = User.objects.create_user(user_name, email, password)
        print('user', user)

        # 设置默认的激活状态为0
        user.is_active = 0
        user.save()

        # 发送激活邮件
        # 1，构建一个邮件要发送的内容
        # a，构建一个用户的数据 data = {"confirm": user.id}
        # b， 用户数据进行加密
        # c,生成一个链接
        # 2，发送邮件
        # 发件邮件的方法（发给谁，发什么什，谁来收）

        # 生成要跳转的页面

        jump_url = reverse("goods:index")
        # 返回响应
        return redirect(jump_url)


# /send_active_code/用户id明文
# def send_active_code(request, uid):


def make_dangerous_code(data):
    """生成临时加密的数据"""
    ser_obj = Serializer("dragonball", 60 * 60 * 2)
    ser_data = ser_obj.dumps(data).decode()
    print('产生的加密数据，两个小时内有效')
    print(ser_data)
    return ser_data


def send_mail():
    pass


# /active/加密的内容{confirm:用户id}
# /user/active/17
class ActiveView(View):
    def get(self, request, info):
        """用户认证"""
        print('来自链接的加密数据info')
        print('info的类型：重要：', type(info))
        print(info)  # {"confirm":id值} 的密文
        ser_obj = Serializer("dragonball")  # 加密器对象
        print('加密器对象创建成功', ser_obj)
        raw_data = ser_obj.loads(info)  # 解密后的数据 {"confirm":id值}
        print('解密码功', raw_data)
        # 用户id提取
        uid = raw_data["confirm"]
        # 根据uid查询用户，得到用户数据，行对象
        try:
            user_line = User.objects.get(id=uid)
        except User.DoesNotExist:
            return HttpResponse("用户不存在")
        else:
            # 行对象.is_active 设置为1
            user_line.is_active = 1
            print('用户激活成功 in try, line....')
            user_line.save()
        # 保存行对象
        # 激活完毕
        return HttpResponse('用户{}激活完毕'.format(uid))


# /user/login
class LoginView(View):
    def get(self, request):
        print('get method')
        print('cookie...', request.COOKIES)
        print('cookie中的remember值', request.COOKIES.get("remember"))

        # 获取用户名
        if "username" in request.COOKIES:
            # {"username":"pyhui"}
            username = request.COOKIES.get("username")
            username = username
            checked = "checked"
        else:
            # {}
            print('cookie里没有存入username')
            username = ""
            checked = ""
        # 渲染页面
        return render(request, "login.html",
                      {"username": username, "checked": checked})

    def post(self, request):
        # 用户登陆
        print('post method')
        print('获取cookie', request.COOKIES)
        print('cookie中的remember值', request.POST.get("remember"))

        # 1，接收数据
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username)
        print(password)
        # 2，校验数据
        from django.contrib.auth import authenticate
        user = authenticate(username=username, password=password)
        # 如果用户验证成功
        if user is not None:
            print('user, is active', user, user.is_active)
            # 如果用户已激活
            if user.is_active:
                # 3，登陆逻辑
                print('登陆用户')
                login(request, user)
                print('页面跳转')

                # 登陆成功后跳转的页面,要么从next里取路径，要反就走默认的路径 首页
                next_url = request.GET.get("next", reverse("goods:index"))
                response = redirect(next_url)
                remember = request.POST.get("remember")
                if remember == 'on':
                    # 响应对象.set_cookie(键，值，过期时间)
                    response.set_cookie("username", username, max_age=7 * 24 * 3600)
                else:
                    response.delete_cookie("username")

                return response
            # 用户未激活
            else:
                # 用户未激活，给他一个链接，让用户点击这个链接就可以发送一个激活邮件
                html = "<a href='/user/resend_active_mail/{}/'>重新发送激活码</a>".format(user.id)
                return render(request, "login.html", {"errmsg": html})
        # 如果用户验证不成功
        else:
            return render(request, "login.html", {"errmsg": "用户名或者密码错误"})

def resend_active_mail(request, uid):
    """ 重新发送激活邮件"""
    # 1，购建一个发送邮件的内容
    # a，构建加密的数据

    mima = make_mima_by_uid(uid)  # str类型的密码
    url = "http://121.40.207.159/user/active/{}".format(mima)
    print('生成的密码是:')
    print(url)
    # 2，发送邮件
    send_register_active_email("364730006@qq.com", uid, url)

    return HttpResponse("resend ok")


def send_register_active_email(to_email, username, url):
    """发送激活邮件"""
    from django.core.mail import send_mail
    from dailyfresh import settings
    subject = "天天生鲜欢迎信息"
    message = ""
    sender = settings.EMAIL_FROM
    receiver = [to_email]
    html_message = '欢迎{0}注册dj鲜生，你的激活链接是<a href="{1}">{1}</a>'.format(username, url)
    send_mail(subject, message, sender, receiver, html_message=html_message)


def make_mima_by_uid(uid):
    """ 生成密码的函数 """
    # 获得一个加密器对象
    # 加密器 = 类名（盐，过期时间）
    obj = Serializer("dragonball", 600)
    # 对数据加密
    data = {"confirm": uid}  # bytes
    mima = obj.dumps(data).decode()
    return mima


from utils.mixin import LoginRequiredMixin


# /user
class UserInfoView(LoginRequiredMixin, View):
# class UserInfoView(View):
    def get(self, request):
        """个人信息显示"""

        # 获取用户个人信息
        user = request.user
        address = Address.objects.get_default_address(user)

        # 获得redis连接
        import django_redis
        conn = django_redis.get_redis_connection('default')

        # 获取数据
        history_key = "history_{}".format(user.id)
        sku_ids = conn.lrange(history_key,0,4)  # [b'6',b'1']

        from goods.models import GoodsSKU
        goods_res = list()
        for id in sku_ids:
            goods = GoodsSKU.objects.get(id=id)
            goods_res.append(goods)
        # 获取用户的历史浏览记录
        return render(request, "user_center_info.html",
                      {'page':'user',
                       'address': address,
                       'goods_li': goods_res
                       })


# /user/order
class UserOrderView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, "user_center_order.html", {'page':'order'})



# /user/address
class AddressView(LoginRequiredMixin, View):

    def get(self, request):
        """获取用户的默认收货地址"""

        # 查找默认地址信息，传模板页
        # 获取用户行对象
        user = request.user
        # try:
        #     # 在地址表中查找，登陆的用户，地址中默认值为True的数据
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 如果查找不到，会进入本分支
        #     address = None

        address = Address.objects.get_default_address(user)

        return render(request, "user_center_site.html",
                      {"address": address, "page":"address"})

    def post(self, request):
        """地址的添加"""
        # 接收数据
        receiver = request.POST.get('receiver')
        addr = request.POST.get('addr')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')
        # 校验数据
        # 1用户提交空数据的判断
        if not all([receiver, addr, phone]):
            return render(request, 'user_center_site.html',
                          {'errmsg': '提交了空数据，数据不完整',
                           "page":"address"}
                          )
        # 2手机号格式验证
        res = re.match(r'^1[3456789]\d{9}$', phone)
        if not res:
            return render(request, 'user_center_site.html',
                          {'errmsg': '手机号格式不正确',
                           "page":"address"}
                          )
        # 业务处理
        # 保存用户提交的地址
        # 情况1，如果用户首次提交地址，让这个地址为默认地址
        # 情况2，如果已经有一个默认地址了，新提交的地址为非默认地址

        # 获取用户行对象
        user = request.user
        # try:
        #     # 在地址表中查找，登陆的用户，地址中默认值为True的数据
        #     address = Address.objects.get(user=user, is_default=True)
        # except Address.DoesNotExist:
        #     # 如果查找不到，会进入本分支
        #     address = None
        address = Address.objects.get_default_address(user)

        # 如果地址查到了，表明用户已经有默认地址了
        if address:
            is_default = False
        else:
            is_default = True

        # 添加地址
        Address.objects.create(
            user=user,
            receiver=receiver,
            zip_code=zip_code,
            phone=phone,
            addr=addr,
            is_default=is_default
        )

        # 返回应答
        # 跳转到用户中心的地址页
        return redirect(reverse('user:address'))


class LogoutView(View):
    def get(self, request):
        """清除用户登陆信息，主要清session"""
        # 清除用户session信息
        logout(request)

        # 跳转到首页
        return redirect(reverse('goods:index'))