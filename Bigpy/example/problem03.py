import requests
import csv
import os
from dotenv import load_dotenv
from enum import Enum

load_dotenv()
API_KEY = os.getenv("OPERNWEATHER_API_KEY")

class Weather(Enum):
    Seoul = "서울"
    Incheon = "인천"
    Busan = "부산"
    Gwangju = "광주"
    Daegu = "대구"

def get_now_weather(city) :
    url = "https://api.openweathermap.org/data/2.5/weather"
    params={
            "q" : city,
            "appid" : API_KEY,
            "exclude" : "current",
            "units" : "metric",
            "lang" : "kr"
    }

    res = requests.get(url, params=params)
    if res.status_code == 404 :
        return None
    res.raise_for_status()
    data = res.json()
    # print(data)
    return data

def get_minmax_temp(weather) :
    high = max(weather, key=lambda x: x["기온"])
    low = min(weather, key=lambda x: x["기온"])

    print(f"가장 더운 도시 : {Weather[high["도시"]].value}, {high["기온"]}")
    print(f"가장 시원한 도시 : {Weather[low["도시"]].value}, {low["기온"]}")

    return high, low

def main() :
    cities = ["Seoul","Incheon","Busan","Gwangju","Daegu"]
    # cities = ["FailTester"]
    results = []
    print("=== 도시별 현재 날씨 ===")
    for city in cities :
        forecast = get_now_weather(city)
        if forecast is None :
            print(f"{city} : 조회 실패")
            continue

        print(f"{Weather[city].value} : {forecast['main']['temp']}도, {forecast['weather'][0]['description']}")
        weather = {
            "도시" : city,
            "기온" : forecast['main']['temp'],
            "날씨" : forecast['weather'][0]['description']
        }
        results.append(weather)
    high, low = get_minmax_temp(results)

    csv_path = "C:/source/pythonsource/Bigpy/py_scrap/data/weather_5cities.csv"
    with open(csv_path, "w", newline="", encoding="utf-8-sig") as f :
        writer = csv.DictWriter(f, fieldnames=["도시","기온","날씨"])
        writer.writeheader()
        writer.writerows(results)


    
    print("종료")

    


        


if __name__ == "__main__" : 
    main()