# import subprocess
import sys
import you_get

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
        # subprocess.getoutput("you-get " + url)
        # os.popen("you-get " + url).read()
        sys.argv = ['you-get', url.strip()]
        print(sys.argv)
        you_get.main() #使用you_get.main()可以在脚本运行时显示you-get的下载情况
    except Exception as e:
        print("下载异常，结束下载......",e)
        exit(-1)


def Engine(fileName):
    urls = ReadUrlsFile(fileName)
    for url in urls:
        DownUseYouGet(url)
        print("完成第{}条记录---{}".format(urls.index(url) + 1, url))

    print("Finished! Thanks!")


if __name__ == '__main__':
    fileName = "urls.txt"
    Engine(fileName)
