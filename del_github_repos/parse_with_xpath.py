from lxml import etree
import os

DIR = "./html_file"
RES_FILE = "del_repos.txt"

file_list = os.listdir(DIR)
# print(file_names)
res_date_list = []  # 存储结果数据

for file in file_list:
    html_tree = etree.parse("{}/{}".format(DIR, file), etree.HTMLParser())
    repnames = html_tree.xpath('//*[@id="org-repositories"]//a[@data-hovercard-type="repository"]/@data-hovercard-url')
    res_date_list.extend(repnames)

    print(file, "finished! 获取元素个数:", len(repnames))



with open(RES_FILE, mode="w", encoding="utf-8") as fw:
    for date in res_date_list:
        # print(date.rsplit('/',1)[0])
        fw.write(date.rsplit('/', 1)[0] + "\n")

print("All finished!")