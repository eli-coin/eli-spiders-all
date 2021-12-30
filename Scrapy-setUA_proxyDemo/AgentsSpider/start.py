from scrapy import cmdline

# cmdline.execute("scrapy genspider bkspider baike.baidu.com".split(" "))
cmdline.execute("scrapy crawl bkspider -o data/res.xml".split(" "))
