from selenium.webdriver.common.by import By
from .authenticate import Authenticate


class Tables(Authenticate):

    def scrape_webpage_for_table(self, header_needed):
        """This method extracts desired table from a page

        :param header_needed: list of header cells or a string representing a cell from the header
        :return: a list of lists consisting of table rows (first list is the header
        """
        tables = self.driver.find_elements(By.XPATH, '//div[./ol]')
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

    def click_table_cell(self, cell_to_identify_row, cell_to_click):
        """
        Method that finds a desired python release and clicks on 'Download' link for that specific release

        Parameters:
            cell_to_identify_row (str): a string containing the desired python release
            cell_to_click (str): a string containing the cell one wants to click
        """
        table = self.driver.find_element(By.XPATH, "//div[./*[text()='Looking for a specific release?']]")
        table_rows = table.find_elements(By.TAG_NAME, 'li')
        desired_row = None

        for row in table_rows:
            if cell_to_identify_row in row.text:
                desired_row = row

        if not desired_row or cell_to_click not in desired_row.text:
            raise ValueError("Introduced values are not in the table or are spelled incorrectly")
        else:
            desired_row.find_element(By.PARTIAL_LINK_TEXT, cell_to_click).click()
