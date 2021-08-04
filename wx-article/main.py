import time
import re
import requests
from jsonpath import jsonpath
from chrome_driver import *


# 获取各部分url，并保存
def get_article_list():
    URL = "https://mp.weixin.qq.com/s?__biz=MzI5MjUzODUxMA==&mid=2247485699&idx=3&sn=82870051419170812af24cb57fcdfe53&chksm=ec7e98e2db0911f4f8bd559f7640e4d29f080e4d5169f2c24c0cede35e3b02d58114d51a95a2&mpshare=1&srcid=0517RiTIH2nASSvZhXasWwf7&sharer_sharetime=1627976726479&sharer_shareid=7c03d1851d17c82121b97b9d9bd3b0e6&from=singlemessage&scene=1&subscene=10000&clicktime=1627976882&enterid=1627976882&ascene=1&devicetype=android-30&version=28000753&nettype=cmnet&abtest_cookie=AAACAA%3D%3D&lang=zh_CN&exportkey=A0IyPuqkZe6bJR4srbMV2lg%3D&pass_ticket=f%2BB9WIPab6r0QUkMyZg5O1Bwd%2BctYR16g9nR0wi11jV0DixI5Vrj5HCV%2FEbNXk7q&wx_header=1"
    driver = ChromeDriverViewer()
    driver.get(URL)
    time.sleep(5)
    a_tag_list = driver.find_elements_by_xpath('//*[@id="js_content"]/p/a')
    with open("urls","w") as fw:
        for a_tag in a_tag_list:
            fw.write(a_tag.get_attribute('href')+"\n")
    driver.close()

# 获取视频url必要的参数vid
def get_vid_from_page(page):
    source_str = 'data-mpvid="wxv_1562705823615778819"'
    pattern = source_str.replace('wxv_1562705823615778819','(.*?)')
    vid = re.findall(pattern,page)[0]

    return vid

# 获取视频url必要的参数mid
def get_mid_from_URL(URL):
    source_str = '&mid=2247485403&'
    pattern = source_str.replace('2247485403', '(.*?)')
    mid = re.findall(pattern, URL)[0]

    return mid

# 获取视频json数据链接
def make_json_req(driver,URL):
    base_url = "https://mp.weixin.qq.com/mp/videoplayer?action={}&mid={}&vid={}"
    action = 'get_mp_video_play_url'
    mid = get_mid_from_URL(URL)

    driver.get(URL)
    time.sleep(3)
    vid = get_vid_from_page(driver.page_source)
    json_req = base_url.format(action,mid,vid)

    return json_req

# 获取mp4原url
def main_get_mp4_url():
    def get_lowwer_qingxidu(json_data):
        video_lowwer2 = jsonpath(json_data, '$..url_info[2].url')
        video_lowwer1 = jsonpath(json_data, '$..url_info[1].url')
        video_lowwer0 = jsonpath(json_data, '$..url_info[0].url')
        if video_lowwer2:
            return video_lowwer2[0]
        elif video_lowwer1:
            return video_lowwer1[0]
        elif video_lowwer0:
            return video_lowwer0[0]
        else:
            print(json_data,"错误！")
            exit(0)

    driver = ChromeDriverNoViewer()

    with open("mp4_urls.txt","w") as fw:
        with open("urls", "r") as fr:
            for link in fr:
                json_req = make_json_req(driver,link.strip())
                json_data = requests.get(json_req).json()  # 获取json数据
                title = jsonpath(json_data, '$.title')[0]
                # url_chaoqing = jsonpath(json_data,'$..url_info[0].url')[0]
                # url_gaoqing = jsonpath(json_data, '$..url_info[1].url')[0]
                # url_liuchang = jsonpath(json_data, '$.url_info[2].url')[0]
                mp4_url = get_lowwer_qingxidu(json_data)
                line = title+"|####|"+mp4_url + "\n"
                fw.write(line)
                print(line,end="")

    driver.close()
    print("Finished!")

"""
# 获取mp3的url必要参数mediaid
def get_mediaid_from_page(page):
    source_str = 'voice_encode_fileid="MzI5MjUzODUxMF8yMjQ3NDg1NDAy"'
    pattern = source_str.replace('MzI5MjUzODUxMF8yMjQ3NDg1NDAy', '(.*?)')
    mediaid = re.findall(pattern, page)[0]
    return mediaid

# 制作mp3对应的url
def make_mediaid_req(URL):
    base_url = "https://res.wx.qq.com/voice/getvoice?mediaid={}"
    driver = ChromeDriverNoViewer()
    driver.get(URL)
    time.sleep(5)
    mediaid = get_mediaid_from_page(driver.page_source)
    mediaid_req = base_url.format(mediaid)

    driver.close()
    return mediaid_req

# # 获取mp3原url（只有部分文章链接有音频，所以还是要下载视频!）
def main_get_mp3_url():
    with open("urls","r") as fr:
        for link in fr:
            mediaid_req = make_mediaid_req(link.strip())
            print(mediaid_req)
            break

def test_has_mp3():
    URL = 'http://mp.weixin.qq.com/s?__biz=MzI5MjUzODUxMA==&mid=2247485636&idx=2&sn=3673236d62a49b0819794c35de2aa728&chksm=ec7e9925db091033f39e6df5fd1a9f40195c026a598757ac4fc7f217d6f6cabae1305daf3738&scene=21#wechat_redirect'
    driver = ChromeDriverNoViewer()
    driver.get(URL)
    time.sleep(5)
    mediaid = get_mediaid_from_page(driver.page_source)
    print(mediaid)
    driver.close()

"""

if __name__ == '__main__':
    # get_article_list()
    main_get_mp4_url()


