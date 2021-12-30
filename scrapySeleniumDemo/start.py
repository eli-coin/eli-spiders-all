from scrapy import cmdline

cmdline.execute("scrapy crawl csdn -o data/res.jl".split(" "))