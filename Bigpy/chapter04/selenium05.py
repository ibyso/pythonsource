from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
import time

chrome_options = Options()
s=Service("./Bigpy/py_scrap/chromedriver/chromedriver.exe")

driver=webdriver.Chrome(service=s,options=chrome_options)

driver.set_window_size(1920,1080)
driver.get('https://google.com')
time.sleep(3) # 대기(모든 load 1초가 걸려도 3초 기다림)
driver.save_screenshot("./Bigpy/py_scrap/img/Website1_3.png")

driver.set_window_size(1920,1080)
driver.get('https://daum.net')
time.sleep(3)
driver.save_screenshot("./Bigpy/py_scrap/img/Website1_4.png")

driver.quit()

print('스크린샷 성공')

# /html/body/div[2]/div[2]/div/div[2]/div/div[1]/div[2]/button[1]