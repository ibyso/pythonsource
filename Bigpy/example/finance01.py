from bs4 import BeautifulSoup
import urllib.request as req
import requests

# 주식 요청 url
url = "https://finance.naver.com/sise/"

# 요청
print(requests.get(url).encoding) # euc-kr

res = req.urlopen(url).read().decode('euc-kr')
# print(res)

soup = BeautifulSoup(res, "html.parser")
table = soup.select("table#siselist_tab_0 tr")
print("오늘의 최고 상한가 종목")
for tr in table :
    tds = tr.select("td")
    if len(tds) >= 4 :
        rank = tds[0].select_one("img").attrs['src'].split("ico_n")[1].split(".")[0]
        title = tds[3].select_one("a.tltle").text
        print(f"{rank}. {title}")

    if tr.find("a") is not None :
        print(tr.select_one(".tltle").string)