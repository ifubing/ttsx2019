"""dailyfresh URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.contrib.auth.decorators import login_required


# 测试视图
from dailyfresh import views

urlpatterns = [
    path('admin/', admin.site.urls),  # 后台管理
    path('test/', views.test),  # 测试视图
    # 127.0.0.1:8000/user/
    # 127.0.0.1:8000/user/logout

    re_path(r'^user/', include('apps.user.urls', namespace='user')),
    # re_path(r'^cart/', include('cart.urls', namespace='cart')),
    # re_path(r'^order/', include('user.order', namespace='order')),
    re_path(r'^', include('apps.goods.urls', namespace='goods')),
    path('tinymce/', include('tinymce.urls')),  # 富文本编辑器
    path('testfather/', views.testfather, name='testfather'),
    path('testson/', views.testson, name='testson'),

]