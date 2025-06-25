from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.google.com")


# Open a webpage
driver.get("https://example.com")

# Get current page title
print(driver.title)

# Get current URL
print(driver.current_url)

# Refresh the page
driver.refresh()

# Navigate to another page
driver.get("https://www.wikipedia.org")

# Go back in browser history
driver.back()

# Go forward
driver.forward()


# Close current tab
driver.close()

# Quit the entire browser
driver.quit()
