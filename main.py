import unittest
from authenticate import Authenticate
from pages.base_page import BasePage
from pages.available_releases import AvailableReleasesPage
from pages.search_results import SearchResultsPage
from pages.first_result import FirstSearchResultPage
import time


class PythonOrg(unittest.TestCase):
    def setUp(self):
        self.driver = Authenticate().open_base_url()

    def test_verify_latest_python_release(self):
        my_release = '3.9'
        my_available_releases_list = [
                                   ['3.9', 'bugfix', '2020-10-05', '2025-10', 'PEP', '596'],
                                   ['3.8', 'bugfix', '2019-10-14', '2024-10', 'PEP', '569'],
                                   ['3.7', 'security', '2018-06-27', '2023-06-27', 'PEP', '537'],
                                   ['3.6', 'security', '2016-12-23', '2021-12-23', 'PEP', '494'],
                                   ['2.7', 'end-of-life', '2010-07-03', '2020-01-01', 'PEP', '373']]

        main_page = BasePage(self.driver)
        # main_page.load()

        main_page.select_base_page_tab_and_click_subtab('downloads', 'All releases')
        newest_python_release = AvailableReleasesPage(self.driver).get_latest_python_release()

        assert my_release == newest_python_release, \
            f"Failed! Most recent release is {newest_python_release} not {my_release}"

        releases_list = AvailableReleasesPage(self.driver).get_info_about_available_releases()

        assert releases_list == my_available_releases_list, \
            "Failed! Actual releases aren't my releases"

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

# ============================================================
    # def test_exercise_1(self):
    #     my_release = '3.9'
    #     exercise1 = Exercise1(self.driver)
    #     assert exercise1.newest_python_release() == my_release, \
    #         f"Failed! Most recent release is '{exercise1.newest_python_release()}' not '{my_release}'"
    #
    # def test_exercise_2(self):
    #     my_example_count = 5
    #     exercise2 = Exercise2(self.driver)
    #     assert exercise2.example_count() == my_example_count, \
    #         f"Failed! Current example count is {exercise2.example_count()} not {my_example_count}"
# ============================================================
    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
