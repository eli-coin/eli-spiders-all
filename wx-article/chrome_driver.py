from selenium import webdriver


# 无界面模式
def ChromeDriverNoViewer():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})  # chromedriver模拟手机浏览器iPhone X
    options.add_argument('--headless') # 无界面设置 1
    options.add_argument('--disable-gpu') # 无界面设置 2
    driverChrome = webdriver.Chrome(executable_path="./tools/chromedriver-linux64", chrome_options=options)
    return driverChrome


# 有界面的就简单了
def ChromeDriverViewer():
    options = webdriver.ChromeOptions()
    options.add_experimental_option('mobileEmulation', {'deviceName': 'iPhone X'})  # chromedriver模拟手机浏览器iPhone X
    driverChrome = webdriver.Chrome("./tools/chromedriver-linux64", chrome_options=options)
    return driverChrome
if __name__ == '__main__':
    print("hello,chrome_drover")
