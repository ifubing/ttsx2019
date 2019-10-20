from django.contrib import admin

# Register your models here.

from goods import models

admin.site.register(models.IndexTypeGoodsBanner)
admin.site.register(models.GoodsType)