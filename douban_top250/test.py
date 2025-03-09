from bs4 import BeautifulSoup
import requests
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}

books_info = {}  # 确保字典不会被覆盖

# 遍历多个分页
for start_num in range(0, 250, 25):
    url = f"https://book.douban.com/top250?start={start_num}"
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"请求失败，状态码：{response.status_code}")
        continue

    soup = BeautifulSoup(response.text, "html.parser")

    # 选择所有 <tr class="item"> 书籍信息块
    books = soup.find_all("tr", class_="item")

    for book in books:
        # 获取书名
        title_tag = book.find("div", class_="pl2").find("a")
        book_title = title_tag.get_text(strip=True) if title_tag else "未知书名"

        # 获取书籍信息
        info_tag = book.find("p", class_="pl")
        book_info = info_tag.get_text(strip=True) if info_tag else "暂无信息"

        # 存入字典
        books_info[book_title] = book_info

    time.sleep(1)  # 添加 1 秒延迟，防止被封

# 打印结果
for book, description in books_info.items():
    print(f"《{book}》: {description}")
