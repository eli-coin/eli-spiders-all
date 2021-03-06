import scrapy
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time


class CsdnSpider(scrapy.Spider):
    name = 'csdn'
    allowed_domains = ['csdn.net']
    start_urls = ['https://passport.csdn.net/newlogin']

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.browser = webdriver.Chrome("./tools/chromedriver.exe")
        self.browser.set_page_load_timeout(30)

    def if_spider_closed(self):
        print("爬虫关闭")
        self.browser.close()# 关闭浏览器

    def parse(self, response):
        with open("./data/res.html","wb") as f:
            f.write(response.body)
