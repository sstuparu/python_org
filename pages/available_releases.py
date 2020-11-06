from selenium.webdriver.common.by import By
from tabulate import tabulate


class AvailableReleasesPage:
    def __init__(self, browser):
        self.browser = browser
        self.available_releases = "//div[./*[text()='Active Python Releases']]/ol"

    def get_latest_python_release(self):
        releases = self.browser.find_element(By.XPATH, self.available_releases)
        newest_release = releases.text.split('\n')[0].split(' ')[0]
        return newest_release

    def get_all_available_releases(self):
        releases = self.browser.find_element(By.XPATH, self.available_releases)
        releases = [el.split(' ', 4) for el in releases.text.split('\n')]
        return releases

    def compare_available_releases(self, input_releases, actual_releases):
        differences = list()
        for i in range(len(input_releases)):
            for j in range(len(input_releases[i])):
                if input_releases[i][j] != actual_releases[i][j]:
                    differences.append(f"Found differences at line {i+1} column {j+1}: {input_releases[i][j]} != "
                                       f"{actual_releases[i][j]}")

        if len(differences) == 0:
            return 'No differences'
        else:
            return differences

    def show_as_table_available_releases(self, table_rows):
        header = ['Python version', 'Maintenance status', 'First released', 'End of support', 'Release schedule']
        return tabulate(table_rows, header)
