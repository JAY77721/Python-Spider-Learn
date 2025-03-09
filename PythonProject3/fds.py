import requests

url = "https://www.google.com/search?q=%E5%91%A8%E6%9D%B0%E4%BC%A6&sca_esv=89edbc9955a427a6&sxsrf=AHTn8zqxXE361xHs3c7dfbTNakvRlpzCsQ%3A1740810890001&ei=iarCZ8ntPMyR4-EPm7fr2Q8&ved=0ahUKEwiJ1uD1oeiLAxXMyDgGHZvbOvsQ4dUDCBE&uact=5&oq=%E5%91%A8%E6%9D%B0%E4%BC%A6&gs_lp=Egxnd3Mtd2l6LXNlcnAiCeWRqOadsOS8pkjMBFAAWABwAHgAkAEAmAG6OqABujqqAQM5LTG4AQPIAQCYAgCgAgCYAwCSBwCgB9gJ&sclient=gws-wiz-serp"
headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"
}
resp = requests.get(url, headers=headers)

# Save the response content to a local HTML file
with open("google_page3.html", "w", encoding="utf-8") as file:
    file.write(resp.text)

print("HTML content saved to google_page.html")
