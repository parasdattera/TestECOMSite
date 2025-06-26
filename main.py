from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from utils.excel_writer import write_to_excel
from utils.logger import get_logger
from config.config import URL, USERNAME, PASSWORD
from tests import test_price_tracker

logger = get_logger()


def get_driver():
    """initialize Chrome first if fails then edge"""
    try:
        logger.info("Trying to launch Chrome in headless mode...")
        # using headless mode to for faster execution
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--headless=new")
        chrome_options.add_argument("--disable-gpu")
        chrome_options.add_argument("--no-sandbox")
        chrome_options.add_argument("--window-size=1920,1080")

        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=chrome_options
        )

    except WebDriverException as ce:
        logger.warning(f"Chrome WebDriver error: {ce}. Trying Edge...")

    except Exception as e:
        logger.error(f"Unexpected error initializing Chrome: {e}", exc_info=True)

    # Try launching Edge
    try:
        edge_options = EdgeOptions()
        edge_options.add_argument("--headless=new")
        edge_options.add_argument("--disable-gpu")
        edge_options.add_argument("--no-sandbox")
        edge_options.add_argument("--window-size=1920,1080")

        return webdriver.Edge(
            service=EdgeService(EdgeChromiumDriverManager().install()),
            options=edge_options
        )

    except WebDriverException as ee:
        logger.error(f"Edge WebDriver error: {ee}", exc_info=True)
    except Exception as e:
        logger.error(f"Unexpected error initializing Edge: {e}", exc_info=True)

    return None  # If both fail


def run_price_tracker():
    logger.info("---------Project Started---------")

    driver = get_driver()
    if not driver:
        logger.critical("Failed to initialize any browser. Exiting script.")
        return

    try:
        logger.info(f"Navigating to {URL}")
        driver.get(URL)

        login_page = LoginPage(driver)
        login_page.login(USERNAME, PASSWORD)

        product_page = ProductPage(driver)
        product_page.sort_by_price_desc()

        product_data = product_page.extract_product_details()
        logger.info(f"Successfully taken {len(product_data)} products.")

        write_to_excel(product_data)
        logger.info("Data is written to excel file successfully.")

    except Exception as e:
        logger.error(f"An error occurred: {e}", exc_info=True)
    finally:
        driver.quit()
        logger.info("Browser session ended.")


if __name__ == '__main__':
    run_price_tracker()
    print("The project run successfully.")
    print("------Starting Running Test of invalid login.------")

    driver = get_driver()  
    success = test_price_tracker.perform_invalid_login_test(driver)
    driver.quit()

    if success:
        print("Invalid login test passed.")
    else:
        print("Invalid login test failed.")

