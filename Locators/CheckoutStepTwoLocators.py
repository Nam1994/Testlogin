from selenium.webdriver.common.by import By

class CheckoutStepTwoLocators(object):
    CANCEL_BUTTON = (By.XPATH, "//div[@class='cart_footer']/a[text()='CANCEL']")
    FINISH_BUTTON = (By.XPATH, "//*[@class='btn_action cart_button']")


class CheckoutComplete(object):
    pass