from selenium.webdriver.common.by import By

class CheckoutStepOneLocators(object):
    INPUT_FIRSTNAME = (By.ID, 'first-name')
    INPUT_LASTNAME = (By.ID, 'last-name')
    INPUT_ZIPCODE = (By.ID, 'postal-code')
    CANCEL_BUTTON = (By.XPATH, "//div[@class='checkout_buttons']/a[text()='CANCEL']")
    CONTINUTE_BUTTON = (By.XPATH, "//*[@class='btn_primary cart_button']")