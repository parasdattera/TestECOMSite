from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, StaleElementReferenceException
)

class ProductPage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

        self.sort_dropdown = (By.XPATH, "//select[@class='product_sort_container']")
        self.product_list = (By.XPATH, "//div[@class='inventory_item']")

    def sort_by_price_desc(self):
        try:
            dropdown = self.wait.until(EC.presence_of_element_located(self.sort_dropdown))
            Select(dropdown).select_by_value("hilo")
        except TimeoutException:
            print("Sort dropdown did not appear in time.")
        except NoSuchElementException:
            print("Sort dropdown not found.")
        except Exception as e:
            print(f"Unexpected error while sorting: {e}")

    def extract_product_details(self):
        data = []
        try:
            products = self.wait.until(EC.presence_of_all_elements_located(self.product_list))
            for p in products:
                try:
                    name = p.find_element(By.CLASS_NAME, "inventory_item_name").text
                    desc = p.find_element(By.CLASS_NAME, "inventory_item_desc").text
                    price = p.find_element(By.CLASS_NAME, "inventory_item_price").text
                    data.append({"name": name, "description": desc, "price": price})
                except NoSuchElementException as e:
                    print(f"Missing product field: {e}")
                except StaleElementReferenceException:
                    print("Product element became stale while accessing it.")
                except Exception as e:
                    print(f"Unexpected error in product parsing: {e}")
        except TimeoutException:
            print("Product list did not load in time.")
        except Exception as e:
            print(f"Unexpected error while fetching product list: {e}")

        return data
