from selenium import webdriver


class Authenticate:
    def open_base_url(self):
        driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe')
        driver.get('https://www.python.org/')
        return driver

