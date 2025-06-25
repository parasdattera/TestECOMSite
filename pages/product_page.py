from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

class ProductPage:
    def __init__(self, driver):
        self.driver = driver
        self.sort_dropdown = (By.CLASS_NAME, "product_sort_container")
        self.product_list = (By.CLASS_NAME, "inventory_item")

    def sort_by_price_desc(self):
        sort_element = Select(self.driver.find_element(*self.sort_dropdown))
        sort_element.select_by_value("hilo")

    def extract_product_details(self):
        products = self.driver.find_elements(*self.product_list)
        data = []
        for p in products:
            name = p.find_element(By.CLASS_NAME, "inventory_item_name").text
            desc = p.find_element(By.CLASS_NAME, "inventory_item_desc").text
            price = p.find_element(By.CLASS_NAME, "inventory_item_price").text
            data.append({"name": name, "description": desc, "price": price})
        return data