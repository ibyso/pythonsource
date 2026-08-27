import requests
import csv
from datetime import datetime, timedelta

# 최근 30일간의 원/달러 환율을 API로 가져와서, 날짜별로 출력하고, 최고/최저 환율과 등락률을 계산한 뒤 CSV로 저장

def get_exchange_rate_trend() :
    end_date = datetime.now().strftime('%Y-%m-%d')
    start_date = (datetime.now() - timedelta(days=30)).strftime('%Y-%m-%d')

    url = f"https://api.frankfurter.dev/v1/{start_date}..{end_date}"
    params = {
        "base": "USD",
        "symbols": "KRW"
    }

    res = requests.get(url, params=params)
    res.raise_for_status()
    data=res.json()
    # print(data)
    rates = data['rates']

    sorted_dates = sorted(rates.keys())

    results =[]
    for date in sorted_dates :
        krw = rates[date]['KRW']
        print(f"{date} : {krw:,.2f}원")
        results.append({"날짜" : date, "환율" : krw})

    max_item = max(rates.items(), key=lambda x : x[1]['KRW'])
    min_item = min(rates.items(), key=lambda x : x[1]['KRW'])

    max_date, max_krw = max_item[0], max_item[1]['KRW']
    min_date, min_krw = min_item[0], min_item[1]['KRW']

    print(f"최고 환율 : {max_krw:,.2f}원 ({max_date})")
    print(f"최저 환율 : {min_krw:,.2f}원 ({min_date})")

    # 첫날 대비 마지막날 등락률
    first_krw = rates[sorted_dates[0]]['KRW']
    last_krw = rates[sorted_dates[-1]]['KRW']
    change_pct = (last_krw/first_krw-1)*100

    sign = "+" if change_pct >= 0 else ""
    print(f"30일간 등락률 : {sign}{change_pct:,.2f}")

    # CSV 저장
    csv_path = "C:/source/pythonsource/Bigpy/py_scrap/data/usd_krw_30days.csv"

    print(f"csv 저장 완료 ")



if __name__ == '__main__' :
    get_exchange_rate_trend()