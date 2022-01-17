import scrapy
from scrapy_redis.spiders import RedisCrawlSpider
from ..items import Jb51Item
from scrapy.spiders import CrawlSpider,Rule # 提取超链接的规则
from scrapy.linkextractors import LinkExtractor # 超链接提取器

class JiaobentitlespiderSpider(RedisCrawlSpider):
    name = 'jiaobenTitleSpider'
    allowed_domains = ['jb51.net']
    start_urls = ['https://www.jb51.net/list/index_96.htm']

    page_categorys = LinkExtractor(allow=(r'/list/list_.+\.htm'), unique=True)  # 图书列表页面
    r1 = Rule(page_categorys, follow=True)
    page_jb = LinkExtractor(allow=(r'/article/\d+\.htm'), unique=True)  # 图书详情页面
    r2 = Rule(page_jb, callback="parse_jb", follow=True)
    # 回调函数处理提取到的链接，follow=True表示一直循环下去
    rules = [r2,r1]

    # 注意:此处要想循环起来，必须修改原来的parse函数函数名,不然循环失败。

    def parse_category(self,response):
        print(response.url)


    def parse_jb(self, response):
        item = Jb51Item()
        # title
        item['title'] = response.xpath('//div[@id="article"]/h1[@class="title"]/text()').extract()[0]
        item['path'] = "".join(response.xpath('//div[@class="breadcrumb"]//text()').extract()[2:]).strip(" \r\n")
        item['url'] = response.url
        print("done:",item['title'])
        yield item
