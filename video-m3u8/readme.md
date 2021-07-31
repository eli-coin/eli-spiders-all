#main.py  
m3u8_url = 'https://xxx/index.m3u8'# m3u8_url文件地址  
video_name = "/home/eli/桌面/projects/eli-spiders-all/video-m3u8/ts_list/hello.mp4"# 要保存的目录+文件名  
down_m3u8(m3u8_url, video_name,AES_key="f6e1ee69bacfaecb")# 调用m3u8下载函数，AES_key是m3u8文件中的.key链接下载下来后文件中的密码  

##mk_ts_url.py  
读取m3u8文件中的ts链接，获取完整的ts下载的url地址  

##down_ts.py  
下载所有的ts片段，并且支持解密  

##decrpyt.py  
AES解密，按照key解密下载下来的ts片段

##config.py  
配置文件，IP代理和UA，代码未完善  


