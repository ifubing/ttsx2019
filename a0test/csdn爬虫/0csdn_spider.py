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



    def get_max_page_number(self, content):
        """获取最大的页码数字"""
        # 具体找最大页码的逻辑，先不写
        return 16


    def parse_url(self, url):
        """发起请求，获取响应"""
        response = requests.get(url)
        content = response.content.decode()
        return content

    def make_list_url(self, max_num):
        """生成列表页的路径列表"""
        for i in range(1, max_num+1):
            temp_url = self.base_url+str(i)+"?"
            self.blog_list_url.append(temp_url)

    def filter_content(self, content):
        """
        根据列表页的html代码，提出每一个贴子的标题和URL
        :param content: 列表页 的HTML代码
        :return:
        """
        h3_list = re.findall(r"<h4>(.*?)</h4>", content, re.DOTALL)
        print('h4 ---------------')
        print(h3_list)


    def parse_blog_list(self):
        """遍历所有的列表，依次解析每一个列表页的内容 """
        for blog in self.blog_list_url:
            # 解析每一个列表页的内容
            content = self.parse_url(blog)
            f = open("a.html", "w", encoding="utf8")
            # 根据列表的内容，解析得到全部的标题和URL
            # print(content)
            self.filter_content(content)

    def start(self):
        """程序启动"""
        # 爬取第一页数据，可以获得这一页的html内容
        print('开始第一页数据的爬取,路径为：')
        print(self.start_page)
        content = self.parse_url(self.start_page)

        # 根据第一页的内容，提取出最大的页码数
        max_num = self.get_max_page_number(content)

        # 根据最大的页码数，知道每一个列表的路径
        self.make_list_url(max_num)

        # 遍历所有的列表，依次解析每一个列表页的内容
        self.parse_blog_list()





        # 通过内容，获取最大的页码数字
        # 【
        # https: // blog.csdn.net / ifubing / article / list / 1?
        # https: // blog.csdn.net / ifubing / article / list / 16?
        # 】
        # url =None
        # content = parse_url(url)
        # 根据列表页的内容，提取文章标题和文章URL




xh = CsdnSpider("qq_43661847")
print(xh.start_page)
xh.start()