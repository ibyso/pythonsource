import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

res = requests.get(url)
soup = BeautifulSoup(res.text,"html.parser")
results = []

books = soup.select('article.product_pod')
rank = 1
for book in books :
    title = book.select_one("h3 a")["title"]
    price = book.select_one("p.price_color").text
    rating = book.select_one("p.star-rating")["class"][1]

    print(f"{rank}. {title} | {price} | 별점 : {rating}")

    data = {
        "순번" : rank,
        "제목" : title,
        "가격" : price,
        "별점" : rating
    }
    results.append(data)
    rank += 1

csv_path = "C:/source/pythonsource/Bigpy/py_scrap/data/books_top20.csv"
with open(csv_path, "w", newline="", encoding="utf-8-sig") as f :
    writer = csv.DictWriter(f, fieldnames=["순번","제목","가격","별점"])
    writer.writeheader()
    writer.writerows(results)

print("csv 저장 완료")
