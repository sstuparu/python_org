from selenium.webdriver.common.by import By


class FirstSearchResultPage:
    def __init__(self, browser):
        self.browser = browser

    def click_on_examples_link(self):
        example_link = 'Examples'
        examples = self.browser.find_element(By.LINK_TEXT, example_link)
        examples.click()

    def count_number_of_examples(self):
        example_id = 'examples'
        li_tag = 'li'

        examples = self.browser.find_element(By.ID, example_id)
        listed_examples = examples.find_elements(By.TAG_NAME, li_tag)

        return len(listed_examples)