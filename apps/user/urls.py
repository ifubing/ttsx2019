from django.urls import path, re_path
from apps.user import views

from django.contrib.auth.decorators import login_required

app_name = "user"
urlpatterns = [
    # path(匹配的路径，函数名)
    # path('register/', views.register, name='register'),  # 后台管理
    path('register/', views.RegisterView.as_view(), name='register'),  # 后台管理
            # '路径', 被装饰器强化了的方法的指向 get方法
    # path('register_handle/', views.register_handle, name='register_handle'),  # 注册处理
    re_path(r'active/(.*)/', views.ActiveView.as_view(), name='active'),  # 用户激活
    path('login/', views.LoginView.as_view(), name='login'),  # 登陆
    re_path(r'resend_active_mail/(\w+)/', views.resend_active_mail, name="resend_active_mail"),  # 重发激活邮件
    # path("",login_required(views.UserInfoView.as_view()), name='user'),
    path("",views.UserInfoView.as_view(), name='user'),
    path("order",views.UserOrderView.as_view(), name='order'),
    path("address",views.AddressView.as_view(), name='address'),
    path("logout",views.LogoutView.as_view(), name='logout'),
]