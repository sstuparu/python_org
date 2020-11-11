from selenium.webdriver.common.by import By
from components.authenticate import Authenticate


class FirstSearchResultPage(Authenticate):

    def click_on_examples_link(self):
        example_link = 'Examples'
        examples = self.driver.find_element(By.LINK_TEXT, example_link)
        examples.click()

    def count_number_of_examples(self):
        example_id = 'examples'
        li_tag = 'li'

        examples = self.driver.find_element(By.ID, example_id)
        listed_examples = examples.find_elements(By.TAG_NAME, li_tag)

        return len(listed_examples)
