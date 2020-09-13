import sys

sys.path.append(".")
import unittest
from selenium import webdriver
from Pages.login_page import LoginPage
from Pages.product_page import ProductPage
from Pages.cart_page import CartPage
from Pages.checkout_step_one_page import CheckoutStepOne
from Pages.checkout_step_two_page import CheckoutStepTwo
from TestCases.base_test import BaseTest
from TestData.TestData import TestData
import time


class SauDemo(BaseTest):
    """A sample test class to show how page object works"""

    @classmethod
    def setUp(self):
        super().setUp(TestData.BROWSER)

    @classmethod
    def tearDown(self):
        super().tearDown()

    def test_product_checout(self):
        login_page = LoginPage(self.driver)
        login_page.login(TestData.USERNAME, TestData.PASSWORD)
        product_page = ProductPage(self.driver)
        for index in enumerate (product_page.get_product_info(), start=1):

            return
        product_page.click_bag_icon()
        time.sleep(2)
        cart_page = CartPage(self.driver)
        time.sleep(2)
        cart_page.click_checkout()
        checkout_step_one_page = CheckoutStepOne(self.driver)
        checkout_step_one_page.addcode(TestData.FIRSTNAME, TestData.LASTNAME, TestData.ZIPCODE)
        checkout_step_one_page.click_continute()
        checkout_step_two_page = CheckoutStepTwo(self.driver)
        checkout_step_two_page.click_finish_button()
        time.sleep(3)


if __name__ == "__main__":
    unittest.main()
