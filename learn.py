import requests
from bs4 import BeautifulSoup

Dcard_article_url = "https://www.dcard.tw/f/pet/p/229834249-%E5%AF%B5%E7%89%A9%E6%BA%9D%E9%80%9A%E9%83%BD%E6%98%AF%E5%81%87%E7%9A%84%E5%8B%B8%E4%B8%96%E6%96%87"

pic = requests.get('https://megapx-assets.dcard.tw/images/60a54f2a-2c99-48c6-b980-83c0b248f7dc/1280.webp') #變數名稱為pic
img2 = pic.content #變數名稱命名為img2

pic_out = open('img1.png','wb') #img1.png為預存檔的圖片名稱
pic_out.write(img2) #將get圖片存入img1.png
pic_out.close() #關閉檔案(很重要)

# payload={ #須送之參數_
#     'from':'/bbs/Gossiping/index.html',
#     'yes':'yes'
# }
# requests.post("https://www.ptt.cc/ask/over18",data=payload) #將參數寫至data

# r = requests.Session()
# r1 = r.post("https://www.ptt.cc/ask/over18?from=%2Fbbs%2FGossiping%2Findex.html",payload) # 按按鈕
# r2 = r.get("https://www.ptt.cc/bbs/Gossiping/index.html") # 爬網址

# soup = BeautifulSoup(r2.text,"html.parser") #將網頁資料轉為html.parser
# sel = soup.select("div.title a") #取HTML標中的 <div class="title"></div> 中的<a>標籤存入sel
# print(type(sel))

# #輸出網頁文章標題
# for s in sel:
#     print(s["href"], s.text)