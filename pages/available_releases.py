from selenium.webdriver.common.by import By
from tabulate import tabulate
from components.authenticate import Authenticate


class AvailableReleasesPage(Authenticate):

    def __init__(self):
        self.available_releases = "//div[./*[text()='Active Python Releases']]/ol"

    # def get_latest_python_release(self):
    #     releases = self.browser.find_element(By.XPATH, self.available_releases)
    #     newest_release = releases.text.split('\n')[0].split(' ')[0]
    #     return newest_release
    #
    # def get_all_available_releases(self):
    #     releases = self.browser.find_element(By.XPATH, self.available_releases)
    #     releases = [el.split(' ', 4) for el in releases.text.split('\n')]
    #     return releases

    def compare_available_releases(self, input_releases, actual_releases):
        differences = list()

        for i in range(len(input_releases)):
            for j in range(len(input_releases[i])):
                if input_releases[i][j] != actual_releases[i][j]:
                    differences.append(f"Found differences at line {i+1} column {j+1}: {input_releases[i][j]} != "
                                       f"{actual_releases[i][j]}")

        if len(differences) == 0:
            return []
        else:
            return differences

    def show_as_table_available_releases(self, content, header):
        # header = ['Python version', 'Maintenance status', 'First released', 'End of support', 'Release schedule']
        return tabulate(content, header)

    # Scrape webpage using soup
    # def scrape_webpage_for_table(self, header_needed):
    #     page = requests.get(self.URL)
    #     soup = BeautifulSoup(page.content, 'html.parser')
    #     results = soup.find(id='content')
    #     headers = results.find_all('div', class_='list-row-headings')
    #     contents = results.find_all('ol', class_='list-row-container menu')
    #     index = ''
    #
    #     for i in range(len(headers)):
    #         header_contents = [cell.text for cell in headers[i].find_all('span')]
    #
    #         if header_needed == header_contents or header_needed in header_contents:
    #             index = i
    #         else:
    #             continue
    #
    #     if index == '':
    #         raise ValueError('No header found or header introduced is incorrect')
    #     else:
    #         header = [cell.text for cell in headers[index].find_all('span')]
    #         content = [[cell.text for cell in row.find_all('span')] for row in contents[index].find_all('li')]
    #         for el in content:
    #             if '' in el:
    #                 el.remove('')
    #         return [header] + content
