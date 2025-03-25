import requests
from bs4 import BeautifulSoup
import json
import pandas

#ptt NBA版網址
url = "https://www.ptt.cc/bbs/NBA/index.html"
#模仿使用者的標記
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}

#讀入網頁原始碼並輸出成一個檔案
ptt_NBA_html = requests.get(url, headers = header)
with open("output.html", "w", encoding = "utf-8") as f:
    f.write(ptt_NBA_html.text)

#爬出每篇文章的html標籤
soup = BeautifulSoup(ptt_NBA_html.text, "html.parser")
articles = soup.find_all("div", class_ = 'r-ent')
data_list = []

for a in articles:
    data = {}
    # 輸出標題
    title = a.find("div", class_ = "title")
    if title and title.a:
        title = title.a.text
    else:
        title = "沒有標題"
    data["標題"] = title
    # 顯示人氣
    popular = a.find("div", class_ = "nrec")
    try:
        if popular and popular.span.text:
            popular = popular.span.text
        else:
            popular = "N/A"
    except:
        popular = "N/A"
    data["人氣"] = popular
    # 顯示日期
    date = a.find("div", class_ = "date")
    if date:
        date = date.text
    else:
        date = "N/A"
    data["日期"] = date
    data_list.append(data)
    print(data)
# 轉成json檔
try:
    with open("ptt_NBA.json", "w", encoding="utf-8") as file:
        json.dump(data_list, file, ensure_ascii=False, indent=4)
    print("done")
except:
    print("error")
#轉成excel檔
try:
    df = pandas.DataFrame(data_list)
    df.to_excel("ptt_NBA.xlsx", index=False, engine="openpyxl")
    print("Done to excel")
except:
    print("failed to excel")