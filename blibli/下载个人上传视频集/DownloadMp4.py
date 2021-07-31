import subprocess


def ReadUrlsFile(fileName):
    """
    获取链接列表
    :param fileName:链接保存文件
    :return:返回列表
    """
    urls = []
    with open(fileName, encoding="utf-8") as fileRead:
        for url in fileRead:
            urls.append(url)

    return urls


def DownUseYouGet(url):
    try:
        subprocess.getoutput("you-get " + url)
        # os.popen("you-get " + url).read()
    except:
        pass


def Engine(fileName):
    urls = ReadUrlsFile(fileName)
    for url in urls:
        DownUseYouGet(url)
        print("完成第{}条记录---{}".format(urls.index(url) + 1, url))

    print("Finished! Thanks!")


if __name__ == '__main__':
    fileName = "urls.txt"
    Engine(fileName)
