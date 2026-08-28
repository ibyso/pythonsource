import requests
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import os
import re
import urllib.request as req
from io import BytesIO # 이미지를 파일로 바로 저장하지 않고 메모리에 바이트로 넣고 다룰 수 있게 함
import xlsxwriter # 엑셀의 텍스트, 이미지까지 셀에 삽입

load_dotenv() # .env 호출
API_KEY = os.getenv("TMDB_API_KEY")

BASE_URL = "https://api.themoviedb.org/3"
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/w500"

# chrome driver 경로 설정
chrome_driver_path="C:/source/pythonsource//Bigpy/py_scrap/chromedriver/chromedriver.exe"

chrome_options = Options()
chrome_options.add_argument("--headless") # 브라우저 창을 띄우지 않음
chrome_options.add_argument("--disable-gpu") # GPU 비활성화
chrome_options.add_argument("--no-sandbox") # 보안 비활성화

s=Service(executable_path=chrome_driver_path)
driver=webdriver.Chrome(service=s,options=chrome_options)

def get_popular_movies(count=5) :
    url = f"{BASE_URL}/movie/popular"
    params = {
        "api_key" : API_KEY,
        "language" : "ko-KR",
        "page" : 1
    }
    res = requests.get(url, params=params)
    res.raise_for_status()
    data = res.json()

    return data['results'][:count]

# 영화 상세 정보
def get_movie_detail(movie_id) :
    url = f"{BASE_URL}/movie/{movie_id}"
    params = {
        "api_key" : API_KEY,
        "language" : "ko-KR",
    }
    res = requests.get(url, params=params)
    res.raise_for_status()
    return res.json()

def get_naver_score(query) :
    try :
        search_query = re.sub(r'[^a-zA-Z0-9가-힣]','',query)+" 영화"  # 검색 정확도 확장
        search_url = f"https://search.naver.com/search.naver?query={search_query}"
        driver.get(search_url)

        time.sleep(3)
        
        try :
            score_element = driver.find_element(By.CLASS_NAME,"area_star_number")
            score = score_element.text.strip()
        except Exception as e :
            score = "평점을 찾을 수 없습니다."

        return score
    except Exception as e :
        return "ERROR"

def get_workbook(obj) :
    try :
        workbook = xlsxwriter.Workbook('C:/source/pythonsource/Bigpy/py_scrap/data/movie_top5.xlsx')
        worksheet = workbook.add_worksheet()

        worksheet.write('A1', '순위')
        worksheet.write('B1', '제목')
        worksheet.write('C1', 'TMDB평점')
        worksheet.write('D1', '개봉일')
        worksheet.write('E1', '네이버평점')
        worksheet.write('F1', '포스터')

        ins_cnt = 2
        for dom in obj :
            try :
                worksheet.write(f'A{ins_cnt}',dom["순위"])
                worksheet.write(f'B{ins_cnt}',dom["제목"])
                worksheet.write(f'C{ins_cnt}',dom["평점"])
                worksheet.write(f'D{ins_cnt}',dom["개봉일"])
                worksheet.write(f'E{ins_cnt}',dom["네이버평점"])

                poster = dom["포스터"]

                if poster and poster.startswith('http') :
                    try :
                        request = req.Request(poster,headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
                        img_data = BytesIO(req.urlopen(request,timeout=10).read())

                        worksheet.insert_image(
                            f"F{ins_cnt}", dom["제목"],
                            {'image_data' : img_data, 'x_scale':0.15, 'y_scale':0.15}
                        )
                    except Exception as e:
                        print(f"이미지 다운로드 실패: {e}")
                        worksheet.write(f'F{ins_cnt}', poster)
                else:
                    worksheet.write(f'F{ins_cnt}', 'None')

                ins_cnt += 1
            except Exception as e:
                print(f"댓글 파싱 오류: {e}")
                continue
        workbook.close()
        return True
    except Exception as e :
        return False


def main() : 
    popular_movies = get_popular_movies(5)

    print("=== 현재 인기 영화 TOP 5 ===\n")
    results = []

    for i, movie in enumerate(popular_movies,1) :
        detail = get_movie_detail(movie['id']) # 영화 아이디로 상세 정보 가져오기

        # 네이버 평점 검색
        score = get_naver_score(detail['title'])

        # 데이터 전처리 구성
        info = {
            "순위" : i,
            "제목" : detail['title'],
            "개봉일" : detail['release_date'],
            "평점" : detail['vote_average'],
            "러닝타임" : f"{detail['runtime']}분",
            "줄거리" : detail['overview'][:80]+"..." if len(detail['overview']) > 80 else detail['overview'],
            "포스터" : IMAGE_BASE_URL + detail['poster_path'] if detail['poster_path'] else None,
            "네이버평점" : score
        }

        print(f"{i}위 | {info['제목']} | 평점 {info['평점']} | 개봉 {info['개봉일']} | 네이버평점 {info['네이버평점']}")
        results.append(info)
    checker = get_workbook(results)
    if checker :
        print("저장 완료")
    else :
        print("저장 실패")


if __name__ == "__main__" :
    try :
        main()
    finally :
        driver.close()