import requests
from bs4 import BeautifulSoup

url = "https://www.dcard.tw/f"

#header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
r = requests.get(url) #將此頁面的HTML GET下來

with open("buying_web.html", "w", encoding = "utf-8") as f:
    f.write(r.text)
# soup = BeautifulSoup(r.text,"html.parser") #將網頁資料轉為html.parser
# sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel

# #輸出網頁文章標題
# for s in sel:
#     print(s["href"], s.text)