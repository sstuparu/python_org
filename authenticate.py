from selenium import webdriver


class Authenticate:
    driver = None

    def create_driver(self):
        if Authenticate.driver == None:
            Authenticate.driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe')

    def close_driver(self):
        Authenticate.driver.close()
        Authenticate.driver = None

    def get_to_web_address(self, URL='https://www.python.org/'):
        self.create_driver()
        Authenticate.driver.get(URL)
        return Authenticate.driver



