import requests
import re

domain = "https://www.dytt8899.com/"
headers = {"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
response = requests.get(domain,headers=headers)
response.encoding = "gbk"

child_hreflist =[]
patern1 = re.compile(r"2025必看热片.*?<ul>(?P<ul>.*?)</ul>",re.S)
patern2 = re.compile(r"href='(?P<href>.*?)'",re.S)
patern3 = re.compile(r"◎片　　名　(?P<片名>.*?)<br />",re.S)
patern4 = re.compile(r'<tbody>.*?<a href="(?P<下载地址>.*?)"',re.S)
result1 = patern1.finditer(response.text)
for item in result1:
    ul = item.group("ul")
result2 = patern2.finditer(ul)
for i in result2:
    #子页面网址
    child_href = domain + i.group("href").strip("/")
    child_hreflist.append(child_href)

for href in child_hreflist:
    child_resp = requests.get(href,headers=headers)
    child_resp.encoding = "gbk"
    # result3 = patern3.finditer(child_resp.text)
    # for item in result3:
    #     print(item.group("片名"))
    # result4 = patern4.finditer(child_resp.text)
    # for item in result4:
    #     print(item.group("下载地址"))

    result3 = patern3.search(child_resp.text)  # 只找第一个匹配项
    if result3:
        print(result3.group("片名"))  # ✅ 只输出第一个匹配的片名

    result4 = patern4.search(child_resp.text)  # 只找第一个匹配项
    if result4:
        print(result4.group("下载地址"))  # ✅ 只输出第一个匹配的下载地址













