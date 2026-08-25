import sys
import io
from bs4 import BeautifulSoup # uv pip install beautifulsoup4


'''
<html>
<body>
<ul id="cars">
  <li id="ge">Genesis</li>
  <li id="av">Avante</li>
  <li id="so">Sonata</li>
  <li id="gr">Grandeur</li>
  <li id="tu">Tucson</li>
</ul>
</body>
</html>
'''

fp = open("./Bigpy/py_scrap/cars.html",encoding="utf-8")
soup = BeautifulSoup(fp, 'html.parser')
# print(soup)

# 함수
def car_func(select) : 
    print("car_func : ",soup.select_one(select).string)

# 메인
car_func("#gr") # 가장 단순
car_func("li#gr")
car_func("ul>#gr")
car_func("#cars #gr")
car_func("li[id='gr']")


# 람다식(매개변수 : q)
car_lambda = lambda q : print("car_lambda : ",soup.select_one(q).string)
car_lambda("#gr")
car_lambda("li#gr")
car_lambda("ul>#gr")


print("car_func : ",soup.select("li")[3].string)
print("car_func : ",soup.find_all("li")[3].string)