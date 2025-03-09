import requests

url = ("https://movie.douban.com/j/search_subjects")
params ={
"type": "movie",
"tag": "热门",
"page_limit": 50,
"page_start": 0,
}

headers = {"user-agent":
"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
resp = requests.get(url,params=params,headers=headers)
print(resp.json())
resp.close()