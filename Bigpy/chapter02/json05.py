import urllib.request as req
import os.path, random
import simplejson as json


# url 요청
url = "https://api.github.com/repositories"

# 경로와 파일명
savename = "./Bigpy/data/repo.json"

# 예외처리
if not os.path.exists(url) : 
    req.urlretrieve(url,savename)

# (1) 객체를 역직렬화(load)
item = json.load(open(savename, 'r', encoding='utf-8'))
print('Type : ',type(item))

for i in item:
    print(i["full_name"] + ' - ' + i["owner"]["url"])


print('-'*20)
# (2) 역직렬화 (loads) - s(string) / 데이터베이스에 이미 저장되어 있는 데이터 읽어오기
items = json.loads(open(savename, 'r', encoding='utf-8').read())
print('Type : ',type(item))

for i in items:
    print(i["full_name"] + ' - ' + i["owner"]["url"])