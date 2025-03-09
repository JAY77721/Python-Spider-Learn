import requests


# 发送GET请求
response = requests.get("https://www.google.com/search?q=github")

# 检查请求是否成功
if response.status_code == 200:
    # 设置保存文件名
    filename = "testst.html"
    # 将内容写入文件
    with open(filename, 'w', encoding=response.encoding) as file:
        file.write(response.text)
    print(f"网页内容已成功保存到 {filename}")
else:
    print(f"请求失败，状态码：{response.status_code}")
