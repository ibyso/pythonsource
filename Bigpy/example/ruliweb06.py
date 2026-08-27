import requests
from bs4 import BeautifulSoup

with requests.Session() as s :
    post_one = s.get("https://bbs.ruliweb.com/market/board/1020/read/37546")