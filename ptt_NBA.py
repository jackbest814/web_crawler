# 請先在terminal安裝requests、bs4、pandas
# 這個程式是ptt NBA版的爬蟲，共爬取十頁
# 取得的資訊有：日期、人氣、標題
# 作者：蔡博硯 製作日期：2025/3/27
# 參考：程式柴python爬蟲教學影片https://www.youtube.com/watch?v=1PHp1prsxIM&t=558s
import requests
from bs4 import BeautifulSoup
import json
import pandas
import time

#ptt NBA版網址
url = "https://www.ptt.cc/bbs/NBA/index.html"
#模仿使用者的標記
header = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36"}
#讀入網頁原始碼
ptt_NBA_html = requests.get(url, headers = header)

# with open("output.html", "w", encoding = "utf-8") as f:
#     f.write(ptt_NBA_html.text)

# 存放資料的位置
data_list = []

# 分析一頁網頁
def analyze(articles):
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

for i in range(10):
    #爬出每篇文章的html標籤
    soup = BeautifulSoup(ptt_NBA_html.text, "html.parser")
    articles = soup.find_all("div", class_ = 'r-ent')
    analyze(articles)
    
    # 換成上一頁
    paging_object = soup.select_one("div.btn-group.btn-group-paging")
    page_bottom_sel = paging_object.find_all("a", class_="btn wide")
    url = "https://www.ptt.cc" + page_bottom_sel[1]["href"]
    
    # 睡一下
    time.sleep(5)


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