from selenium.webdriver.common.by import By


class SearchResultsPage:
    def __init__(self, browser):
        self.browser = browser

    def click_first_result(self):
        first_search_result = '// *[ @ id = "content"] / div / section / form / ul / li[1] / h3 / a'
        first_result = self.browser.find_element(By.XPATH, first_search_result)
        first_result.click()