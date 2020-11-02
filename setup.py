from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


class Exercise1:

    def __init__(self, driver):
        self.driver = driver
        self.downloads = 'downloads'
        self.all_releases = '//*[@id="downloads"]/ul/li[1]/a'
        self.available_releases = '//*[@id="content"]/div/section/div[1]/ol'

    def newest_python_release(self):
        # Find 'Downloads' and 'All Releases'
        downloads = self.driver.find_element(By.ID, self.downloads)
        all_releases = self.driver.find_element(By.XPATH, self.all_releases)

        # Click on 'All Releases'
        actions = ActionChains(self.driver)
        actions.move_to_element(downloads).move_to_element(all_releases).click().perform()

        # Get the newest Python release
        available_releases = self.driver.find_element(By.XPATH, self.available_releases)
        newest_release = available_releases.text.split('\n')[0].split(' ')[0]

        return newest_release


class Exercise2:

    def __init__(self, driver):
        self.driver = driver
        self.search_input = 'decorator'
        self.search_bar = 'id-search-field'
        self.content = 'content'
        self.search_results = 'li'
        self.example_link = 'Examples'
        self.examples = 'examples'

    def example_count(self):
        # Search 'decorator'
        search_bar = self.driver.find_element(By.ID, self.search_bar)
        search_bar.clear()
        search_bar.send_keys(self.search_input)
        search_bar.send_keys(Keys.RETURN)

        # Get the first result and click on it
        content = self.driver.find_element(By.ID, self.content)
        first_result = content.find_element(By.TAG_NAME, self.search_results)
        first_result_link = self.driver.find_element(By.LINK_TEXT, first_result.text.split('\n')[0])
        first_result_link.click()

        # Click on 'Examples' link
        examples_link = self.driver.find_element(By.LINK_TEXT, self.example_link)
        examples_link.click()

        # Find the examples and return the number of examples
        examples = self.driver.find_element(By.ID, self.examples)
        example_list = examples.find_elements(By.TAG_NAME, self.search_results)

        return len(example_list)
