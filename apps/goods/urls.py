from django.contrib import admin
from django.urls import path, re_path, include
# from apps.user import views
from apps.goods import views

# app_name = "user"
app_name = "goods"
urlpatterns = [
    # path('register/', views.register, name='register'),  # 后台管理
    # path('register_handle/', views.register_handle, name='register_handle'),  # 注册处理
    # re_path(r'^$', views.index, name='index'),
    re_path(r'^$', views.IndexView.as_view(), name='index'),
]
