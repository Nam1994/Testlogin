from selenium.webdriver.common.by import By

class CartLocators(object):
    CHECKOUT_BUTTON = (By.XPATH, "//*[@class='btn_action checkout_button']")
    CONTINUTE_BUTTON_SHOPPING = (By.XPATH, "//*[@class='btn_secondary']")

    def REMOVE_TO_CART_BUTTON(index):
        x = "//div[@class='cart_list']//div[@class='cart_item']["
        z = "]//button[text()='REMOVE']"
        return (By.XPATH, (x + str(index) + z))