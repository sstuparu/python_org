from selenium.webdriver.common.by import By


class FirstSearchResult:
    def __init__(self, browser):
        self.browser = browser
        self.example_link = 'Examples'
        self.example_id = 'examples'
        self.li_tag = 'li'

    def click_on_examples_link(self):
        examples = self.browser.find_element(By.LINK_TEXT, self.example_link)
        examples.click()

    def count_number_of_examples(self):
        examples = self.browser.find_element(By.ID, self.example_id)
        listed_examples = examples.find_elements(By.TAG_NAME, self.li_tag)

        return len(listed_examples)