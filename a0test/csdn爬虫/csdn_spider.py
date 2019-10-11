# 面向对向，爬取一个博客的全部内容
# https://blog.csdn.net/ifubing/article/list/1?
# https://blog.csdn.net/pyyyyyyy/article/list/1?

import requests
import re

class CsdnSpider:
    def __init__(self, username):
        # 博客列表页的基本路径
        self.base_url = "https://blog.csdn.net/{}/article/list/".format(username)

        # 博客列表起始页的路径
        self.start_page = self.base_url+ "1?"
        # self.start_page = "https://blog.csdn.net/{}/article/list/1?".format(username)

        # 博客的全列表页路径列表
        self.blog_list_url = []  # 博客列表页的

        # 所有文章的路径列表，结构为列表包字典
        # [{"title":"python-描述符", "url":"http://www.xxxx.com"},{}]
        self.article_data = []  # 博客中文章与URL的数据集合


    def start(self):
        """程序启动"""
        # 一，爬取列表第一页URL，获得html内容
        # # start_html = self.parse(第一页URL)
        #
        # 二，解析第一页的响应html内容，构建所有文章列表URL列表
        # make_blog_list_url(start_html)
        # 方法主要功能：
        # 1，得最大一页的页码值
        # 2，根据最大一页的页码值以及根据博文列表路径规律，拼出所有博文列表的URL
        # 3，把所有的博文列表URL添加到列表self.blog_list_url中
        #
        # 三，根据 self.blog_list_url ，对每一个博客列表页进行爬取
        # 每一个博客列表中，都有很多博客文章信息
        # 每爬取一个博客列表，都要把文章信息进行一个获取
        # 每一篇博客文章的数据构建成字典结构  例如{"title":"爬虫-发起get请求", "url":"http...."}
        # 把所有的文章数据添加到对象的属性  self.article_data 中
        #
        # 四，根据文章信息列表 self.article_data 发起一个又一个的请求
        # 把每一个博客文章请求的内容保存到本地文件中
        # 保存的文件名称格式：
        # 博文名称.html
        pass


obj = CsdnSpider("ifubing")
print(obj.start_page)
