import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")


book = soup.find('article',class_='product_pod')
book_a = book.find('h3')
title = book_a.find('a')
print(title.attrs['title'])