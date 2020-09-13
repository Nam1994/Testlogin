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

    def PRODUCT_NAME(index):
         x = "//*[@class = 'inventory_item']["
         y = "]//div[@class= 'inventory_item_name']"
         return (By.XPATH, (x + str(index) + y))

    def PRODUCT_DESC(index):
         x = "//*[@class = 'inventory_item']["
         y = "]//div[@class= 'inventory_item_desc']"
         return (By.XPATH, (x + str(index) + y))

    def PRODUCT_PRICES(index):
         x = "//*[@class = 'inventory_item']["
         y = "]//div[@class= 'inventory_item_price']"
         return (By.XPATH, (x + str(index) + y))

    def PRODUCT_IMAGE(index):
        x = "//*[@class = 'inventory_item']["
        y = "]//div[@class= 'inventory_item_img']"
        return (By.XPATH, (x + str(index) + y))