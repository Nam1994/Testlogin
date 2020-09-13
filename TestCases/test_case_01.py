import sys

sys.path.append(".")
import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from TestCases.base_test import BaseTest
from TestData.TestData import TestData


class SauDeMo(BaseTest):
    """A sample test class to show how page object works"""

    @classmethod
    def setUp(self):
        super().setUp(TestData.BROWSER)

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_login_successfully(self):
        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        product_page = ProductPage(self.driver)
        product_page.product_text()
        print(product_page.product_text())
        self.assertEqual(product_page.product_text(), 'Products')
if __name__ == "__main__":
    unittest.main()
