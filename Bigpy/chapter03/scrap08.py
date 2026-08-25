import sys
import io
import urllib.request
import urllib.parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup


url = "https://www.encar.com"

# encar 처럼 봇 차단이 있는 사이트는 기본 User-Agent로 요청하면
# 403/406 보안에러가 발생하여 정상 페이지를 받지못함
req = urllib.request.Request(
    url,
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/124.0.0.0 Safari/537.36"
    }
)

mem = urllib.request.urlopen(req)
print(type(mem))
print("geturl :",mem.geturl())
print("status :",mem.status)

print("headers :",mem.getheaders())
print("info :",mem.info()) # header 정보를 행 단위로 보여줌
print("getcode :",mem.getcode())

# 서버가 사용하는 문자 인코딩, 없으면 utf-8
encoding = mem.info().get_content_charset() or 'utf-8'

# 바이트를 500개만 자르면 멀티바이트(한글, 한자, 특문) 중간에 끊김
# unicodeDecodeError가 날 수 있으므로 errors = 'ignore'처리
raw = mem.read(500)
print("read :",raw.decode(encoding,errors='ignore'))

print(urlparse('https://www.encar.com?test=test').query)


