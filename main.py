import unittest
from selenium import webdriver
from setup import *


class PythonOrg(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Program Files (x86)\chromedriver.exe')
        self.driver.get('https://www.python.org/')

    def test_exercise_1(self):
        my_release = '3.9'
        exercise1 = Exercise1(self.driver)
        assert exercise1.newest_python_release() == my_release, \
            f"Failed! Most recent release is '{exercise1.newest_python_release()}' not '{my_release}'"

    def test_exercise_2(self):
        my_example_count = 5
        exercise2 = Exercise2(self.driver)
        assert exercise2.example_count() == my_example_count, \
            f"Failed! Current example count is {exercise2.example_count()} not {my_example_count}"

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
