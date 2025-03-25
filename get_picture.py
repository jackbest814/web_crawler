import requests
from bs4 import BeautifulSoup
import json

Dcard_pet_url = "https://www.dcard.tw/f/pet"

url = requests.get(Dcard_pet_url)
soup = BeautifulSoup(url.text, "html.parser")
#將首頁文章的網址放入list
sel = soup.select("div.PostList_wrapper_2BLUM a.PostEntry_root_V6g0r")
title_list=[]
for s in sel:
    title_list.append(s["href"])
url = "https://www.dcard.tw"+ title_list[2]