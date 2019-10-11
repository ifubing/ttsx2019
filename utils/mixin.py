from django.contrib.auth.decorators import login_required


class LoginRequiredMixin(object):
    @classmethod
    def as_view(cls, **kwargs):
        """调用父类的as_view"""
        # view = super(LoginRequiredMixin, cls).as_view(**kwargs)
        view = super().as_view(**kwargs)
        return login_required(view)

#
# # /user
# class UserInfoView(LoginRequiredMixin, View):
# # class UserInfoView(View):
#     def get(self, request):
#         """个人信息显示"""
#
#         # 获取用户个人信息
#         user = request.user
#         address = Address.objects.get_default_address(user)
#
#         # 获取用户的历史浏览记录
#         return render(request, "user_center_info.html",
#                       {'page':'user',
#                        'address': address
#                        })
#
#
# UserInfoView.as_view()   #  被装饰器强化了的方法的指向 get方法
