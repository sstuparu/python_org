from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class BasePage:
    URL = 'https://www.python.org/'
    SEARCH_INPUT = (By.ID, 'id-search-field')

    def __init__(self, browser):
        self.browser = browser

    def load(self):
        self.browser.get(self.URL)

    def search(self, phrase):
        search_bar = self.browser.find_element(*self.SEARCH_INPUT)
        search_bar.clear()
        search_bar.send_keys(phrase + Keys.RETURN)

    def hover_over_and_click(self, field, sub_field):
        element = self.browser.find_element(By.ID, field)
        sub_element = self.browser.find_element(By.XPATH, sub_field)

        actions = ActionChains(self.browser)
        actions.move_to_element(element).move_to_element(sub_element).click().perform()
