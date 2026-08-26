from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

chrome_options = Options()
s=Service("./Bigpy/py_scrap/chromedriver/chromedriver.exe")

driver=webdriver.Chrome(service=s,options=chrome_options)

driver.get('https://google.com')
driver.save_screenshot("./Bigpy/py_scrap/img/Website1_1.png")

driver.get('https://daum.net')
driver.save_screenshot("./Bigpy/py_scrap/img/Website1_2.png")

driver.quit()

print('스크린샷 성공')