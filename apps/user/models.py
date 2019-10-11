from django.db import models
from django.contrib.auth.models import AbstractUser
from db.base_model import BaseModel
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from django.conf import settings

class User(AbstractUser, BaseModel):
    """用户模型类"""

    def generate_active_token(self):
        """生成用户签名字符串"""
        serializer = Serializer(settings.SECRET_KEY, 3600)
        info = {'confirm': self.id}
        token = serializer.dump(info)
        return token.decode()

    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name


class AddressManager(models.Manager):
    """地址视图的模型类管理器"""
    def get_default_address(self, user):
        """获取用户的默认收货地址"""
        try:
            # address = Address.objects.get(user=user, is_default=True)
            # address = self.model.objects.get(user=user, is_default=True)
            address = self.get(user=user, is_default=True)
        except Address.DoesNotExist:
            address = None

        return address


class Address(BaseModel):
    """地址模型类"""
    user = models.ForeignKey("User", verbose_name="所属帐户", on_delete=models.CASCADE)
    receiver = models.CharField(max_length=20, verbose_name="收件人", )
    addr = models.CharField(max_length=256, verbose_name="收货地址")
    zip_code = models.CharField(max_length=6, null=True, verbose_name="邮政编码")
    phone = models.CharField(max_length=11, verbose_name="联系电话")
    is_default = models.BooleanField(default=False, verbose_name="是否默认")

    objects = AddressManager()  # 绑定模型类管理器

    class Meta:
        db_table = "df_address"
        verbose_name = "地址"
        verbose_name_plural = verbose_name


from tinymce.models import HTMLField
class MceTest(models.Model):
    status_choices = (
        (0,'good'),
        (1,'bad')
    )
    status = models.SmallIntegerField(default=1, choices=status_choices)
    detail = HTMLField(verbose_name='测试富文本')

    class Meta:
        db_table = "df_test_mcd"
        verbose_name = "test_mce"
        verbose_name_plural = verbose_name