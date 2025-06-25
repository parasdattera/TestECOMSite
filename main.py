from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.excel_writer import write_to_excel
from utils.logger import get_logger
from config.config import URL, USERNAME, PASSWORD

logger = get_logger()

def main():
    logger.info("Starting ECOM Price Tracker")
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(URL)
    login = LoginPage(driver)
    login.login(USERNAME, PASSWORD)

    product_page = ProductPage(driver)
    product_page.sort_by_price_desc()
    data = product_page.extract_product_details()
    logger.info(f"Extracted {len(data)} products.")

    write_to_excel(data)
    logger.info("Written data to Excel file.")
    driver.quit()

if __name__ == '__main__':
    main()