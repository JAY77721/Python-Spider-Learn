import requests

url = "https://fanyi.baidu.com/sug"
s= input("输入s")
data = {
    "kw":s
}
headers = {"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
resp = requests.post(url, data=data, headers=headers)
print(resp.json())