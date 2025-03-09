import requests

proxies = {
    "http": "http://127.0.0.1:7890",
    "https": "http://127.0.0.1:7890",
}
headers = {"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"}

response = requests.post("http://www.google.com/", proxies=proxies,headers=headers)
response.encoding = "utf-8"
print(response.status_code)
