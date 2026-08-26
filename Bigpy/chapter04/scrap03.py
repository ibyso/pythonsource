import requests, json
# 쿠키 활용, 타임아웃 설정, post 요청으로 데이터 전송 문법

# 쿠키 객체 생성
jar = requests.cookies.RequestsCookieJar()
# /cookies 경로에서 사용할 쿠키 설정(예: name=kim)
jar.set('name','kim',domain='httpbin.org',path='/cookies')

r = requests.get('https://httpbin.org/cookies',cookies=jar)
r.raise_for_status()
# print(r.text)

# timeout 설정
# 3초 안에 응답하지 않으면 예외처리하고 강제 종료
r = requests.get('https://github.com',timeout=3)
# print(r.text)

# post 요청하면서도 데이터도 보낼 수 있음
r = requests.post('https://github.com',data={'name':'kim'},cookies=jar)
# print(r.text)

payload1 = {'key1':'values1','key2':'values2'}      # dict
payload2 = (('key1','values1'),('key2','values2'))  # tuple
payload3 = {'key1':'values1'}


r = requests.post('https://httpbin.org/post',data=payload1)
print(r.text)
print("-"*20)
r = requests.post('https://httpbin.org/post',data=payload1)
print(r.text)