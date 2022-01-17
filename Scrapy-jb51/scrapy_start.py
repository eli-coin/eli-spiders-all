from scrapy import cmdline
from os import system

def del_data():
    """删除原数据文件"""
    try:
        system("del data.jl")
        print("data文件删除")
    except:
        print("文件删除失败")
# cmdline.execute("scrapy crawl batspider".split(" "))


del_data() # 删除原数据文件
cmdline.execute("scrapy crawl jiaobenTitleSpider -o data.jl -s FEED_EXPORT_ENCODING=utf-8".split(" "))
# cmdline.execute("scrapy crawl myspider -o data.jl -s FEED_EXPORT_ENCODING=utf-8".split(" "))
# cmdline.execute("scrapy crawl myspider -o data.csv -s FEED_EXPORT_ENCODING=utf-8".split(" "))
# cmdline.execute("scrapy crawl myspider -o data.xml -s FEED_EXPORT_ENCODING=utf-8".split(" "))