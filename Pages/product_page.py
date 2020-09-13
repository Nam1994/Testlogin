from Pages.base_page_object import BasePage
from Locators.ProductLocators import ProductLocators
from Objects.product import Product
import logging


class ProductPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    def add_product_to_cart(self, index):
        # print("Productpage:" + str(index))
        self.click(ProductLocators.ADD_TO_CART_BUTTON(index))

    def click_bag_icon(self):
        logging.info("ADD a cart")
        self.click(ProductLocators.ICON_BAGE)

    def remove_add_to_cart(self, index):
        # print("Productpage:" + str(index))
        self.click(ProductLocators.REMOVE_TO_CART_BUTTON(index))

    def product_text(self):
        return self.get_text(ProductLocators.LABEL_PRODUCT)

    def get_product_name(self, index):
        return self.get_text(ProductLocators.PRODUCT_NAME(index))

    def get_product_desc(self, index):
        return self.get_text(ProductLocators.PRODUCT_DESC(index))

    def get_product_price(self, index):
        return self.get_text(ProductLocators.PRODUCT_PRICES(index))

    def get_product_image(self, index):
        return self.get_text(ProductLocators.PRODUCT_IMAGE(index))

    def get_product_info(self, index):
        name = self.get_product_name(index)
        price = self.get_product_price(index)
        desc = self.get_product_desc(index)
        product = Product(name, desc, price, 1)

        return product




