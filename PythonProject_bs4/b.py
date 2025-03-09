import requests
from bs4 import BeautifulSoup

url = "http://umei.cc/bizhitupian/xiaoqingxinbizhi/"
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text
soup = BeautifulSoup(html, 'html.parser')
alist = soup.find("div",attrs={"class":"item_list infinite_scroll"}).find_all("a")
# print(alist)

for a in alist:
    child_hred = "http://umei.cc/" + a['href']
    child_response = requests.get(child_hred)
    child_response.encoding = 'utf-8'
    child_html = child_response.text
    child_soup = BeautifulSoup(child_html, 'html.parser')
    pic = child_soup.find("div",attrs={"class":"big-pic"})
    img = pic.find("img").get('src')
    print(img)
    img_resp = requests.get(img)
    img_resp.encoding = 'utf-8'
    img_name = img.split('/')[-1]
    with open("img/"+img_name, 'wb') as f:
        f.write(img_resp.content)
        print("over!!!",img_name)

print("all done")
#不能爬全部
