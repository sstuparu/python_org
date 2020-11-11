import unittest
from components.authenticate import Authenticate
from pages.base_page import BasePage
from pages.available_releases import AvailableReleasesPage
from pages.search_results import SearchResultsPage
from pages.first_result import FirstSearchResultPage
from components.tables import Tables
import datetime


class PythonOrg(unittest.TestCase):
    main_page_obj = BasePage()
    tables_obj = Tables()
    search_result_page_obj = SearchResultsPage()
    first_result_page_obj = FirstSearchResultPage()

    def setUp(self):
        Authenticate().create_driver()
        Authenticate().get_to_web_address()

    def test_verify_latest_python_release(self):
        """
        Steps:
        1. Go to 'Downloads' -> 'All releases' page
        2. Extract the latest python release and verify it is 3.9
        """
        my_release = '3.9'

        my_available_releases_list = [
                                   ['3.9', 'bugfix', '2020-10-05', '2025-10', 'PEP 596'],
                                   ['3.8', 'bugfix', '2019-10-14', '2024-10', 'PEP 569'],
                                   ['3.7', 'security', '2018-06-27', '2023-06-27', 'PEP 537'],
                                   ['3.6', 'security', '2016-12-23', '2021-12-23', 'PEP 494'],
                                   ['2.7', 'end-of-life', '2010-07-03', '2020-01-01', 'PEP 373']]

        self.main_page_obj.select_base_page_tab_and_click_subtab('downloads', 'All releases')

        releases_list = self.tables_obj.scrape_webpage_for_table('Python version')
        newest_python_release = releases_list[1][0]

        assert my_release == newest_python_release, \
            f"Failed! Most recent release is {newest_python_release} not {my_release}"

        verdict = AvailableReleasesPage().compare_available_releases(my_available_releases_list,
                                                                     releases_list[1::])
        assert verdict == [], \
            f"Failed! Actual differences are:\n {[el for el in verdict]}"

    def test_verify_example_count_is_5(self):
        """
        Steps:
        1. Search for word 'decorator' on main page
        2. Click on first result
        3. Verify the no. of displayed examples is 5
        """
        my_example_no = 5

        self.main_page_obj.search_for_keyword('decorator')

        self.search_result_page_obj.click_first_result()

        self.first_result_page_obj.click_on_examples_link()

        actual_example_no = self.first_result_page_obj.count_number_of_examples()

        assert my_example_no == actual_example_no, \
            f"Failed! The actual example no is {actual_example_no} not {my_example_no}"

    # def test_compare_table_cells(self):
    #     available_releases_obj = AvailableReleasesPage(self.driver)
    #     table1 = available_releases_obj.scrape_webpage_for_table('Python version')
    #     table2 = available_releases_obj.scrape_webpage_for_table('Release version')
    #
    #     date1 = datetime.datetime.strptime(table1[1][2], '%Y-%m-%d')
    #     date2 = datetime.datetime.strptime(table2[1][1], '%b. %d, %Y')
    #
    #     assert date1 == date2, \
    #         f"Failed! The two cells don't contain same info: {table1[1][2]} != {table2[1][1]}"

    def test_compare_table_cells(self):
        """
         1. Go to 'Downloads' -> 'All releases' page
         2. Extract the two tables present on the page
         3. Compare the date cells from the first row of both tables and see that are similar
        """

        self.main_page_obj.select_base_page_tab_and_click_subtab('downloads', 'All releases')

        table1 = self.tables_obj.scrape_webpage_for_table('Python version')
        table2 = self.tables_obj.scrape_webpage_for_table('Release version')

        date1 = datetime.datetime.strptime(table1[1][2], '%Y-%m-%d')
        date2 = datetime.datetime.strptime(table2[1][1], '%b. %d, %Y')

        assert date1 == date2, \
            f"Failed! The two cells don't contain same info: {table1[1][2]} != {table2[1][1]}"

    def test_verify_correspondence_between_tables(self):
        """
        1. Go to 'Downloads' -> 'All releases' page
        2. Extract the two tables present on the page
        3. Verify each version of Python from the first table has at least one correspondence in the second table
        """
        self.main_page_obj.select_base_page_tab_and_click_subtab('downloads', 'All releases')

        correspondence_dict = dict()

        table1 = self.tables_obj.scrape_webpage_for_table('Python version')
        table2 = self.tables_obj.scrape_webpage_for_table('Release version')

        for row_table1 in table1[1:]:
            for row_table2 in table2[1:]:
                if not correspondence_dict.get(row_table1[0]) and row_table1[0] in row_table2[0]:
                    correspondence_dict[row_table1[0]] = [] + [row_table2[0]]
                elif correspondence_dict.get(row_table1[0]) and row_table1[0] in row_table2[0]:
                    correspondence_dict[row_table1[0]].append(row_table2[0])
                else:
                    continue

        for key in correspondence_dict:
            assert correspondence_dict.get(key), \
                f"Key {key} not found in dictionary"

    def tearDown(self):
        Authenticate().close_driver()


if __name__ == "__main__":
    unittest.main()
