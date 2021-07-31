import requests

def MakeUrlsWithPageNum(formatUrl,start: int, end: int):
    """
    根据页码制作格式化的链接
    :param start: 页码第一页
    :param end: 页码最后一页
    :return: 生成的链接列表
    """
    urls = []
    for i in range(start,end+1):
        urlTmp = formatUrl.format(i)
        urls.append(urlTmp)

    return urls

def WriteToFile(fileName:str,objUrls: list):
    """
    将制作的格式化链接保存到文件中
    :param UrlsList: 链接列表
    :return:None
    """
    with open(fileName,"a",encoding="utf-8") as fileOpen:
        for objUrl in objUrls:
            fileOpen.write(objUrl+"\n")


def Engine(fileName,formatUrl):
    """
    爬虫引擎
    :return:
    """
    urls = MakeUrlsWithPageNum(formatUrl,1,11)
    print("\n".join(urls))
    WriteToFile(fileName, urls)
    print("Finished! 总共生成记录条数：{}".format(len(urls)))

if __name__ == '__main__':
    formatUrl = "https://www.bilibili.com/video/BV1ts411G7ZD?p={}"
    fileName = "urls.txt"
    Engine(fileName,formatUrl)