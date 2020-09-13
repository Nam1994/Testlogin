from selenium.webdriver.common.by import By

class ProductLocators(object):
    ICON_BAGE = (By.XPATH, "//*[@class='shopping_cart_container']")
    LABEL_PRODUCT = (By.XPATH, "//div[@class='product_label']")

    def ADD_TO_CART_BUTTON(index):
        x = "//div[@class='inventory_list']/div[@class='inventory_item']["
        z = "]//button[text()='ADD TO CART']"
        # print("abc" + str(index))
        # print(x + str(index) + z)
        return (By.XPATH, (x + str(index) + z))

    def REMOVE_TO_CART_BUTTON(index):
        x = "//div[@class='inventory_list']/div[@class='inventory_item']["
        z = "]//button[text()='REMOVE']"
        return (By.XPATH, (x + str(index) + z))


class CartLocators(object):
    CHECKOUT_BUTTON = (By.XPATH, "//*[@class='btn_action checkout_button']")
    CONTINUTE_BUTTON_SHOPPING = (By.XPATH, "//*[@class='btn_secondary']")

    def REMOVE_TO_CART_BUTTON(index):
        x = "//div[@class='cart_list']//div[@class='cart_item']["
        z = "]//button[text()='REMOVE']"
        return (By.XPATH, (x + str(index) + z))


class CheckoutStepOneLocators(object):
    INPUT_FIRSTNAME = (By.ID, 'first-name')
    INPUT_LASTNAME = (By.ID, 'last-name')
    INPUT_ZIPCODE = (By.ID, 'postal-code')
    CANCEL_BUTTON = (By.XPATH, "//div[@class='checkout_buttons']/a[text()='CANCEL']")
    CONTINUTE_BUTTON = (By.XPATH, "//*[@class='btn_primary cart_button']")


class CheckoutStepTwoLocators(object):
    CANCEL_BUTTON = (By.XPATH, "//div[@class='cart_footer']/a[text()='CANCEL']")
    FINISH_BUTTON = (By.XPATH, "//*[@class='btn_action cart_button']")


class CheckoutComplete(object):
    pass
