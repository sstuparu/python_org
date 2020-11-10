import unittest
from components.authenticate import Authenticate
from pages.base_page import BasePage
from pages.available_releases import AvailableReleasesPage
from pages.search_results import SearchResultsPage
from pages.first_result import FirstSearchResultPage
from components.tables import Tables
import datetime


class PythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = Authenticate().get_to_web_address()

    def test_verify_latest_python_release(self):
        my_release = '3.9'

        my_available_releases_list = [
                                   ['3.9', 'bugfix', '2020-10-05', '2025-10', 'PEP 596'],
                                   ['3.8', 'bugfix', '2019-10-14', '2024-10', 'PEP 569'],
                                   ['3.7', 'security', '2018-06-27', '2023-06-27', 'PEP 537'],
                                   ['3.6', 'security', '2016-12-23', '2021-12-23', 'PEP 494'],
                                   ['2.7', 'end-of-life', '2010-07-03', '2020-01-01', 'PEP 373']]

        main_page = BasePage(self.driver)
        main_page.select_base_page_tab_and_click_subtab('downloads', 'All releases')

        available_releases_obj = Tables(self.driver)
        releases_list = available_releases_obj.scrape_webpage_for_table('Python version')
        newest_python_release = releases_list[1][0]

        assert my_release == newest_python_release, \
            f"Failed! Most recent release is {newest_python_release} not {my_release}"

        verdict = AvailableReleasesPage(self.driver).compare_available_releases(my_available_releases_list,
                                                                                releases_list[1::])
        assert verdict == [], \
            f"Failed! Actual differences are:\n {[el for el in verdict]}"

    def test_verify_example_count_is_5(self):
        my_example_no = 5

        main_page = BasePage(self.driver)
        # main_page.load()
        main_page.search_for_keyword('decorator')

        search_result = SearchResultsPage(self.driver)
        search_result.click_first_result()

        first_result_page = FirstSearchResultPage(self.driver)
        first_result_page.click_on_examples_link()

        actual_example_no = first_result_page.count_number_of_examples()

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
        main_page = BasePage(self.driver)
        main_page.select_base_page_tab_and_click_subtab('downloads', 'All releases')

        available_releases_obj = Tables(self.driver)
        table1 = available_releases_obj.scrape_webpage_for_table('Python version')
        table2 = available_releases_obj.scrape_webpage_for_table('Release version')

        date1 = datetime.datetime.strptime(table1[1][2], '%Y-%m-%d')
        date2 = datetime.datetime.strptime(table2[1][1], '%b. %d, %Y')

        assert date1 == date2, \
            f"Failed! The two cells don't contain same info: {table1[1][2]} != {table2[1][1]}"

    def tearDown(self):
        Authenticate().close_driver()


if __name__ == "__main__":
    unittest.main()
