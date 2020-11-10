from selenium.webdriver.common.by import By


class Tables:
    def __init__(self, browser):
        self.browser = browser

    def scrape_webpage_for_table(self, header_needed):
        """This method extracts desired table from a page

        :param header_needed: list of header cells or a string representing a cell from the header
        :return: a list of lists consisting of table rows (first list is the header
        """
        tables = self.browser.find_elements(By.XPATH, '//div[./ol]')
        headers = [table.find_element(By.CLASS_NAME, 'list-row-headings') for table in tables]
        contents = [table.find_element(By.TAG_NAME, 'ol') for table in tables]
        index = ''

        for i in range(len(headers)):
            header_contents = [cell.text for cell in headers[i].find_elements(By.TAG_NAME, 'span')]

            if header_needed == header_contents or header_needed in header_contents:
                index = i
                break
            else:
                continue

        if index == '':
            raise ValueError('No header found or header introduced is incorrect')
        else:
            header = [cell.text for cell in headers[index].find_elements(By.TAG_NAME, 'span')]
            content = [[cell.text for cell in row.find_elements(By.TAG_NAME, 'span') if cell.text != ''] for row in
                       contents[index].find_elements(By.TAG_NAME, 'li')]

            return [header] + content
