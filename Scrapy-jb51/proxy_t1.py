import requests

proxies={"https":"https://proxy.it.taikang.com:8080"}
url = "https://www.runoob.com/"
res = requests.get(url,proxies=proxies).content.decode("utf-8")
print(res)

