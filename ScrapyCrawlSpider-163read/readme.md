# 网易云阅读数目信息详情抓取
        bookid
        book名称
        bookURL
        book作者
        book类型
        book状态
        book更新时间
        book字数
        book封面
        book点击量
        book评分人数
        book评分

### 那么,如何限制深度爬虫的深度呢??? 总不可以一直往深处抓下去吧!


## scrapy 踩坑:
### 1，不要覆盖重写（spider.py文件中）parse方法，否则 CrawlSpider 会失去它原有的功效。  
    你应该写一些自己的新的 parse_func 函数，而不是使用parse.  
    要避免使用 parse 作为回调函数，由于 CrawlSpider 使用 parse 方法来实现其逻辑，如果你将其覆盖，CrawlSpider将失去功效.  

### 2，CrawlSpider是一匹野马，使用时一定要注意：
    A，设计尽量精确的爬取规则，减少爬网数量
    B，降低蜘蛛的并发频率。
    C,设置延迟,不要过度访问网站,增加服务器压力.[形同攻击]