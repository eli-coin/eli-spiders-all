# encoding=utf-8
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from PIL import Image
from GET_headers import getheaders


# 无界面模式
def chrome_driver_NoView():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome(executable_path="./tools/chromedriver", chrome_options=chrome_options)
    return driver


# 有界面模式
def chrome_driver_View():
    driver = webdriver.Chrome("./tools/chromedriver")
    return driver


def get_snap(driver):  
    """
    对目标网页进行截屏。这里截的是全屏
    """
    driver.save_screenshot('full_snap.png') # 保存截的是全屏
    page_snap_obj = Image.open('full_snap.png')
    return page_snap_obj


def get_image_with_driver(driver):
    """
    对图片所在位置进行定位，然后从全屏截图中截取图片
    """
    html_img = driver.find_element_by_id('address')
    time.sleep(2)
    location = html_img.location
    print(location)
    size = html_img.size
    left = location['x']
    top = location['y']
    right = left + size['width']
    bottom = top + size['height']

    page_snap_obj = get_snap(driver)
    image_obj = page_snap_obj.crop((left, top, right, bottom)) # 从全屏截图中截取图片
    # image_obj.show() # 显示截取的图片(使用系统程序打开image_obj)
    image_obj.save("tiny_snap.png") # 保存截取的图片
    return image_obj  # 得到的就是验证码


def start():
    # driver = chrome_driver_View()  # 设置driver 模拟浏览器程序
    driver = chrome_driver_NoView()
    """更换headers"""
    user_agent = getheaders()
    options = webdriver.ChromeOptions()
    options.add_argument('user-agent=%s' % user_agent)
    driver.get("http://www.dianping.com/shop/97141937")  # 模拟浏览器访问url
    get_image_with_driver(driver)

    driver.close()  # 关闭模拟器


if __name__ == '__main__':
    start()
