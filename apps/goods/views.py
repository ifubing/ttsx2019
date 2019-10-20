from django.shortcuts import render
from django.shortcuts import HttpResponse
from django.shortcuts import redirect
from django.views.generic import View
from goods import models
# Create your views here.

# def index(request):
#     return render(request, "index.html")

class IndexView(View):
    """首页"""
    def get(self,request):
        """ 显示首页 """

        # 获取商品的种类信息
        types = models.GoodsType.objects.all()

        # 获取轮播商品信息 IndexGoodsBanner
        # 先查询得到查询集，然后再排序，升序排序
        # 查询全部：模型类.objects.all()
        # 排序：查询集.order_by(字段)，升序排。  降序排：查询集.order_by(-字段)
        goods_banners = models.IndexGoodsBanner.objects.all().order_by("index")


        # 获取首页促销信息
        # 查询出全部，然后再排序
        promotion_banners = models.IndexPromotionBanner.objects.all().order_by("index")


        # 获取首页分类商品展示信息
        type_goods_banners = models.IndexTypeGoodsBanner.objects.all()
        # 此处为所有的商品种类行对象中，添加首页需要展示的商品信息
        for type in types:  # 虽然不该与关键词重名，不过这里不用type功能，不影响使用
            # 获取图片展示的商品
            image_branners = type_goods_banners.filter(type=type, display_type=1)
            # 获取文本展示的商品
            title_banners = type_goods_banners.filter(type=type, display_type=0)
            # 给种类对象添加属性
            type.image_banners = image_branners
            type.title_banners = title_banners

        # 获取购物车商品的数目
        # 暂时以0代替
        cart_count = 0

        # 组织模板上下文
        context = {
            "types": types,
            "goods_banners": goods_banners,
            "promotion_banners":promotion_banners,
            # "type_goods_banners": type_goods_banners,
            "cart_count":cart_count
        }

        # 渲染模板
        return render(request, "index.html", context)
