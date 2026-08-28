import requests
import json
import os
from dotenv import load_dotenv
from collections import defaultdict # 키가 없어도 에러 없이 빈 리스트를 만들어주는 딕셔너리

load_dotenv()
API_KEY = os.getenv("OPERNWEATHER_API_KEY")

def get_5day_forecast(city) :
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params={
        "q" : city,
        "appid" : API_KEY,
        "units" : "metric",
        "lang" : "kr"
    }

    res = requests.get(url, params=params)
    if res.status_code == 404 :
        return None
    res.raise_for_status()
    data = res.json()
    # print(data)

    # 3시간 간격 데이터를 날짜별로 묶어서 평균/최고/최저 계산
    daily = defaultdict(list)

    for item in data['list'] : 
        date = item['dt_txt'].split(" ")[0]
        daily[date].append(item)

    results = []
    for date, items in daily.items() :
        temps = [i['main']['temp'] for i in items]
        weather_desc = items[len(items)//2]['weather'][0]['description']

        results.append({
            "날짜" : date,
            "최고기온" : round(max(temps),1),
            "최저기온" : round(min(temps),1),
            "날씨":weather_desc
        })

    return results


def main() :
    city = "Seoul"
    forecast = get_5day_forecast(city)
    # print(forecast)

    # 예외처리
    if forecast is None :
        print("도시를 찾을 수 없음")
        return

    print(f"=== {city} 5일 일기예보")
    for day in forecast :
        print(f"{day['날짜']} | 최고 {day['최고기온']}도 | 최저 {day['최저기온']}도 | {day['날씨']}")

    with open("C:/source/pythonsource/Bigpy/py_scrap/data/weather_5days.json","w", encoding="utf-8") as f :
        json.dump(forecast, f, ensure_ascii=False, indent=2)

    print("\n 저장완료")


if __name__ == "__main__" : 
    main()