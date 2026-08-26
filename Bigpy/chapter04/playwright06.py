from playwright.sync_api import sync_playwright
# uv pip install playwright
# python -m playwright install chromium

with sync_playwright() as p :
    browser = p.chromium.launch()
    page = browser.new_page()

    page.goto('https://google.com')
    page.wait_for_timeout(3000)
    page.screenshot(path="./Bigpy/py_scrap/img/Web1.png")

    page.goto('https://daum.net')
    page.wait_for_timeout(3000)
    page.screenshot(path="./Bigpy/py_scrap/img/Web2.png")

    browser.close()

print("성공")