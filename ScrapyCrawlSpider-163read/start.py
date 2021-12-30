from scrapy import cmdline

cmdline.execute("scrapy crawl myspider -o data/res.jl -s FEED_EXPORT_ENCODING=utf-8".split(" "))