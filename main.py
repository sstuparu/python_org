import unittest
from selenium import webdriver
from pages import *
import time


class PythonOrg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe')
        #self.driver.get('https://www.python.org/')

    def test_verify_latest_python_release(self):
        my_release = '3.9'

        main_page = base_page.BasePage(self.driver)
        main_page.load()

        main_page.hover_over_and_click('downloads', '//*[@id="downloads"]/ul/li[1]/a')
        newest_python_release = available_releases.AvailableReleases(self.driver).get_latest_python_release()

        assert my_release == newest_python_release, \
            f"Failed! Most recent release is {newest_python_release} not {my_release}"

    def test_verify_example_count_is_5(self):
        my_example_no = 5

        main_page = base_page.BasePage(self.driver)
        main_page.load()
        main_page.search('decorator')

        search_result = search_results.SearchResults(self.driver)
        search_result.click_first_result()

        first_result_page = first_result.FirstSearchResult(self.driver)
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
