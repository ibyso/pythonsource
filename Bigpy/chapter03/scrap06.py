import sys
import io
import urllib.request
import urllib.parse
from urllib.parse import urlparse
from bs4 import BeautifulSoup


# 내 공인 주소를 알려주는 API
API = "https://api.ipify.org"

# 딕셔너리
values ={
    'format' : 'json'
}

print('before',values)
params = urllib.parse.urlencode(values)
print('after',params)