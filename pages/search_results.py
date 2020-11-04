from selenium.webdriver.common.by import By


class SearchResults:
    def __init__(self, browser):
        self.browser = browser
        self.first_search_result = '// *[ @ id = "content"] / div / section / form / ul / li[1] / h3 / a'

    def click_first_result(self):
        first_result = self.browser.find_element(By.XPATH, self.first_search_result)
        first_result.click()