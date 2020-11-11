from selenium.webdriver.common.by import By
from components.authenticate import Authenticate


class SearchResultsPage(Authenticate):

    def click_first_result(self):
        # first_search_result = '// *[ @ id = "content"] / div / section / form / ul / li[1] / h3 / a'
        first_search_result = "//div//form/ul//a"
        first_result = self.driver.find_element(By.XPATH, first_search_result)
        first_result.click()
