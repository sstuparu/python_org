from selenium.webdriver.common.by import By


class AvailableReleasesPage:
    def __init__(self, browser):
        self.browser = browser
        self.available_releases = '//*[@id="content"]/div/section/div[1]/ol'

    def get_latest_python_release(self):
        releases = self.browser.find_element(By.XPATH, self.available_releases)
        newest_release = releases.text.split('\n')[0].split(' ')[0]
        return newest_release

    def get_info_about_available_releases(self):
        releases = self.browser.find_element(By.XPATH, self.available_releases)
        releases = [el.split(' ') for el in releases.text.split('\n')]
        return releases
