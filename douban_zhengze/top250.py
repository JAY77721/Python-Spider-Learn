import requests
import re
import csv

for start in range(0, 250, 25):
    url = f"https://movie.douban.com/top250?start={start}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
    }

    # 发送请求
    resp = requests.get(url, headers=headers)
    resp.encoding = 'utf-8'  # 确保正确解析中文

    # 正则表达式匹配电影名、导演、评价人数
    pattern = re.compile(
        r'<span class="title">(?P<title>[^<]+)</span>.*?'
        r'导演:\s*(?P<director>[^&]+)&nbsp;.*?'
        r'(?P<ratings>\d+)人评价',
        re.S
    )

    # 提取匹配结果
    movies = pattern.finditer(resp.text)


    # 输出电影信息
    # for movie in movies:
        # title = movie.group("title").strip()
        # director = movie.group("director").strip()
        # ratings = movie.group("ratings").strip()
        # print(f"电影名: {title}, 导演: {director}, 评价人数: {ratings}")
    with open("no1douban_top250.csv", mode="a", newline="", encoding="utf-8") as f:
        csvWriter = csv.DictWriter(f, fieldnames=["title", "director", "ratings"])
        csvWriter.writeheader()  # 写入表头

        for movie in movies:
            movie_dict = movie.groupdict()  # 获取匹配结果字典
            csvWriter.writerow(movie_dict.st)  # 写入CSV

print("数据写入完成！")
print("over")