import sys
import io
from bs4 import BeautifulSoup

html = '''
<html>
<body>
    <h1>Find VS Select 차이</h1>
    <p>css 선택자를 사용 및 다중반환</p>
    <p>태그 선택자 사용 및 단일반환</p>
</body>
</html>
'''


soup = BeautifulSoup(html, 'html.parser')
# print('html ->',html)
# print('-'*20)
# print('soup -> ',type(soup))
# print(soup)
# print('-'*20)
print('prettify',soup.prettify())


print('-'*20)
h1 = soup.html.body.h1
print(h1)
p1 = soup.html.body.p
print("p1 -> ",p1)
p2 = p1.next_sibling.next_sibling
print("p2 -> ",p2)
p3 = p1.previous_sibling.previous_sibling
print("p3 -> ",p3)