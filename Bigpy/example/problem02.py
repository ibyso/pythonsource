import requests
import json
from datetime import datetime, timedelta


def get_exchange_rate_trend() :

    url = f"https://api.frankfurter.dev/v1/latest"
    params = {
        "base": "USD",
        "symbols": "KRW,JPY,EUR"
    }

    res = requests.get(url, params=params)
    res.raise_for_status()
    data=res.json()
    print(data)

    rate = [{
        'KRW':data['rates']['KRW'],
        'JPY':data['rates']['JPY'],
        'EUR':data['rates']['EUR'],
        'checked_date' : datetime.now().strftime("%Y-%m-%d")
    }]
    for k, v in data['rates'].items() :
        print(f"1 USD = {data['rates'][k]} {k}")


    # print(f"1 USD = {data['rates']['KRW']}KRW")
    # print(f"1 USD = {data['rates']['EUR']}EUR")
    # print(f"1 USD = {data['rates']['JPY']}JPY")

    with open("C:/source/pythonsource/Bigpy/py_scrap/data/exchange_today.json","w", encoding="utf-8") as f :
        json.dump(rate, f, ensure_ascii=False, indent=2)

    print("\n 저장완료")



if __name__ == '__main__' :
    get_exchange_rate_trend()