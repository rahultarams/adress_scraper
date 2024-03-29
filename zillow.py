import sys
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class WebScraper:
    def __init__(self, url):
        # Set up Firefox WebDriver
        service = Service('/path/to/geckodriver')  # Specify the path to geckodriver
        options = webdriver.FirefoxOptions()
        options.headless = True
        options.add_argument("--disable-gpu")  # Disable GPU hardware acceleration
        options.add_argument("--window-size=1920,1080")  # Specify window size

        # Set up Selenium with Firefox WebDriver and options
        self.driver = webdriver.Firefox(service=service, options=options)

        # Set default timeouts
        self.implicit_wait_timeout = 30
        self.explicit_wait_timeout = 60

        # Navigate to the provided URL
        self.navigate_to_page(url)

    def __del__(self):
        # Close the browser when the object is deleted
        self.driver.quit()

    def navigate_to_page(self, url):
        self.driver.get(url)
        self.driver.implicitly_wait(self.implicit_wait_timeout)

    def find_address(self):
        try:
            wait = WebDriverWait(self.driver, self.explicit_wait_timeout)
            address_tag = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'h2[data-test-id="bdp-building-address"]')))
            address_text = address_tag.text.strip()
            return address_text
        except TimeoutException:
            print("Timed out waiting for address element to load")
            return None

if __name__ == "__main__":
    # Check if a URL has been provided as a command-line argument
    if len(sys.argv) < 2:
        print("Usage: python script_name.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    scraper = WebScraper(url)
    address = scraper.find_address()
    if address:
        print("Address:", address)
    else:
        print("Address not found.")
