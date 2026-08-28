from bs4 import BeautifulSoup
from playwright.sync_api import sync_playwright

import os
from dotenv import load_dotenv
load_dotenv() # .env 호출

def main() :
    with sync_playwright() as p : # platwright 세션 활용
        browser = p.chromium.launch(
            headless=False,     # 화면 보이기
            # 소리끄기, 리눅스 권한 문제 방지, 공유 메모리 부족 방지, GPU 비활성화
            args=[
                "--mute-audio",
                "--no-sandbox",
                "--disable-dev-shm-usage",
                "--disable-gpu",
            ]
        )
        page = browser.new_page(viewport={"width":1920,"height":1280})

        page.goto('https://www.casetify.com/samsung/galaxy-z-flip8-cases?')
        page.wait_for_timeout(5000)

        # 키보드의 page down 키를 눌러서 스크롤 수행
        page.keyboard.press("PageDown")
        page.wait_for_timeout(2000)

        scroll_pause_time = 4000
        last_height = page.evaluate("document.documentElement.scrollHeight")

        limit = 5 # 무한 스크롤 방지용

        while True :
            page.evaluate("window.scrollTo(0,document.documentElement.scrollHeight)")
            page.wait_for_timeout(scroll_pause_time)

            new_height = page.evaluate("document.documentElement.scrollHeight")
            print(f"Last height : {last_height}, Current Height: {new_height}")

            if new_height == last_height :
                break
            if limit <=0 :
                break
            
            last_height = new_height
            limit -= 1

        html_content = page.content()
        browser.close()

    soup = BeautifulSoup(html_content, "html.parser")
    titles = soup.select('div.listing-product-container p.artwork-desc')
    print(f"\n총 상품 수 : {len(titles)}개\n")

    with open("C:/source/pythonsource/Bigpy/py_scrap/data/titles.txt","w",encoding="UTF-8") as f :
        for title in titles :
            f.write(f"{title.string}\n")

    print("저장 완료")


if __name__ == "__main__" :
    main()