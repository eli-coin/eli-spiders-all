# Scrapy设置代理与UA(User-agent)

## scrapy设置UA和代理步骤
### 1,
settings.py文件加入代理和agents，见settings.py文件末尾

### 2，
新建/修改middlewares.py文件【此处是建立一个文件夹，收录middlewares】  
```
--middlewares  
    --RandomProxy.py  
    --RandomUserAgent.py (推荐使用 fake-useragent 包来自动获取UA  )
```

### 3，
settings.py文件中，激活中间件：middlewares
'AgentsSpider.middlewares.RandomUserAgent.RandomUserAgent': 100, # 规定，修改Agent，序号为100
'AgentsSpider.middlewares.RandomProxy.RandomProxy': 200, # 规定，修改代理，序号为200

### 完成!



## 但是,其实!!!scrapy只需要一行代码就可以自动设置UA，利用一款名为 scrapy-fake-useragent 的包:
```pip install scrapy-fake-useragent``` 

在settings.py中间件处加入一行代码,直接使用 scrapy_fake_useragent 包中封装好的中间件，设置UA。

```
DOWNLOADER_MIDDLEWARES = {
'scrapy.downloadermiddlewares.useragent.UserAgentMiddleware':None,# 关闭默认方法
'scrapy_fake_useragent.middleware.RandomUserAgentMiddleware':400,# 开启第三方库的中间件
}
```