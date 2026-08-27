import requests
from bs4 import BeautifulSoup

with requests.Session() as s :
    #게시글 가져오기
    post_one = s.get("https://bbs.ruliweb.com/market/board/1020/read/37546")

    post_one.raise_for_status
    print(post_one)

    print("----------------")
    soup = BeautifulSoup(post_one.text,"html.parser")

    # 문서출력
    article = soup.select("#board_read > div > div.board_main > div.board_main_view > div.view_content > article > div > p")
    print(article)

    # string 처리
    # string : 태그 안에 순수 텍스트만 가져오기 나머지는 None 처리됨()
    for i in article :
        if i.string is not None and i.img == None :
            print(i.string)
