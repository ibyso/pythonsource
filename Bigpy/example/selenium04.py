from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import re

# chrome driver 경로 설정
chrome_driver_path="C:/source/pythonsource//Bigpy/py_scrap/chromedriver/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--headless") # 브라우저 창을 띄우지 않음
chrome_options.add_argument("--disable-gpu") # GPU 비활성화
chrome_options.add_argument("--no-sandbox") # 보안 비활성화

s=Service(executable_path=chrome_driver_path)
driver=webdriver.Chrome(service=s,options=chrome_options)

try :
    # 영화 검색 페이지 열기(에 : "말할 수 없는 비밀")
    search_query = "말할 수 없는 비밀 영화 평점"
    search_url = f"https://search.naver.com/search.naver?query={search_query}"
    driver.get(search_url)

    time.sleep(3)

    # 영화 제목 가져오기
    try :
        title_element = driver.find_element(By.CLASS_NAME,"title_area")
        title = title_element.text.strip()
    except Exception as ex :
        title = "제목을 찾을 수 없습니다."

    # 영화 평점 가져오기
    try :
        score_element = driver.find_element(By.CLASS_NAME,"area_star_number")
        score = score_element.text.strip()
    except Exception as ex :
        score = "평점을 찾을 수 없습니다."

    # 결과 출력
    print(f"영화 제목 : {title}")
    print(f"평점 : {score}")

    # 특수 문자 제거
    filename = re.sub(r'[^a-zA-Z0-9가-힣]','',title)

    # 평점만 파일로 저장
    file_path = os.path.join(os.getcwd(),f"{filename}.txt")
    with open(file_path, "w", encoding="utf-8") as f :
        f.write(score)

except Exception as e :
    pass
finally :
    driver.close()