import requests


url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude" : 37.5665,
    "longitude" : 126.9780,
    "hourly" : "temperature_2m",
    "timezone" : "Asia/Seoul"
}

res = requests.get(url,params=params)
data = res.json()

times = data["hourly"]['time']
temps = data["hourly"]['temperature_2m']

for t, temp in zip(times, temps) :
    print(f"{t} : {temp}도")

print("최고 기온 :",max(temps))
print("최저 기온 :",min(temps))