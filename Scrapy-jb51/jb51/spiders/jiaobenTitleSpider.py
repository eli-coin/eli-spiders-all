import scrapy


class JiaobentitlespiderSpider(scrapy.Spider):
    name = 'jiaobenTitleSpider'
    allowed_domains = ['jb51.net']
    start_urls = ['https://www.jb51.net/list/index_96.htm']

    def parse(self, response):
        print(response.url)
        print(response.content)
        pass
