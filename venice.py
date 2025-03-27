# 請先在terminal安裝requests、bs4、pandas
import requests
import time
from bs4 import BeautifulSoup
import pandas

# 威尼斯電影第三頁
url = "https://www.venice-cinemas.com.tw/movie.php?page=3"
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
          'Priority': 'u=0, i',
          'referer': 'https://www.venice-cinemas.com.tw/movie.php?state=&page=1',
          'sec-ch-ua': '\"Chromium\";v=\"134\", \"Not:A-Brand\";v=\"24\", \"Microsoft Edge\";v=\"134\"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '\"Windows\"',
          'sec-fetch-dest': 'document',
          'sec-fetch-mode': 'navigate',
          'sec-fetch-site': 'same-origin',
          'sec-fetch-user': '?1',
          'upgrade-insecure-requests': '1',
          'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
          'accept-language': 'zh-TW,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6'}
# 存放所有資料的位置
data_list = []

# 分析一頁網頁
def analyze(soup):
    info = soup.find_all("div", class_="col-md-10 col-sm-9")
    for i in info:
        # 存放資料
        data = {}
        # 抓取標籤h2裡a標籤的電影名稱
        title = i.select_one("h2 a")
        if title and title.text:
            data["電影名稱"] = title.text
        else:
            data["電影名稱"] = "沒有名字"
        
        # 抓取第一個ul標籤裡li標籤裡的電影資訊
        entry = i.find_all("ul", class_="entry-meta clearfix")
        entry_list = entry[0].find_all("li")
        data["上映日期"] = entry_list[0].text
        data["片長"] = entry_list[1].text
        data["級數"] = entry_list[2].text
        data["瀏覽人數"] = entry_list[3].text
        
        # 資料匯出到全域變數
        data_list.append(data)


# 爬取三頁資料
for i in range(1, 4):
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.text, "html.parser")
    if response.status_code == 200:
        analyze(soup)
    else:
        print("no")
        break
    
    # 切換到上一頁
    next_bottom_sel = soup.select_one("ul.pagination")
    next_bottom = next_bottom_sel.select_one("li a")
    url = "https://www.venice-cinemas.com.tw/movie.php" + next_bottom["href"]
    
    # 避免快速爬取引起網管注意
    time.sleep(5)

# 匯出成excel檔
df = pandas.DataFrame(data_list)
df.to_excel("venice.xlsx", index=False, engine="openpyxl")
print("Done to excel")    
                   

# url = "https://www.venice-cinemas.com.tw/movie.php?page=1"
# url2 = "https://www.venice-cinemas.com.tw/movie.php?page=2"
# url3 = "https://www.venice-cinemas.com.tw/movie.php?page=3"
# response = requests.get(url, headers=header)
# soup = BeautifulSoup(response.text, "html.parser")
# if response.status_code == 200:
#     a = soup.find_all("div", class_="row movie-list bottommargin-sm")
#     for b in a:
#         print(b.text)
# else:
#     print("no")

# response2 = requests.get(url2, headers=header)
# soup = BeautifulSoup(response2.text, "html.parser")
# if response2.status_code == 200:
#     a = soup.find_all("div", class_="row movie-list bottommargin-sm")
#     for b in a:
#         print(b.text)
# else:
#     print("no")

# response3 = requests.get(url3, headers=header)
# soup = BeautifulSoup(response3.text, "html.parser")
# if response3.status_code == 200:
#     a = soup.find_all("div", class_="row movie-list bottommargin-sm")
#     for b in a:
#         print(b.text)
# else:
#     print("no")
