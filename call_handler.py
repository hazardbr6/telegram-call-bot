import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller

# Automatically install/update ChromeDriver
chromedriver_autoinstaller.install()

# Setup Chromium options for headless mode and optimized performance
options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialize the WebDriver (Chromium)
driver = webdriver.Chrome(options=options)

# List of free calling websites
CALLING_SITES = [
    "https://globfone.com/call-phone/",
    "https://www.poptox.com/",
    "https://www.citrus.tel/",
    "https://www.voipdiscount.com/",
    "https://www.dingtone.me/"
]

def make_call(phone_number):
    for site in CALLING_SITES:
        try:
            driver.get(site)
            time.sleep(5)  # Wait for the page to load
            if "globfone" in site:
                driver.find_element("name", "phoneNumber").send_keys(phone_number)
                driver.find_element("id", "callButton").click()
            elif "poptox" in site:
                driver.find_element("id", "phoneNumber").send_keys(phone_number)
                driver.find_element("id", "callButton").click()
            elif "citrus" in site:
                driver.find_element("name", "phone").send_keys(phone_number)
                driver.find_element("id", "callNow").click()
            elif "voipdiscount" in site:
                driver.find_element("name", "phone").send_keys(phone_number)
                driver.find_element("id", "startCall").click()
            elif "dingtone" in site:
                driver.find_element("id", "phoneInput").send_keys(phone_number)
                driver.find_element("id", "startCall").click()
            time.sleep(10)  # Allow time for call initiation
            return True, site
        except Exception as e:
            # Optionally log error: print(f"Error on {site}: {e}")
            continue  # Try the next website if one fails
    return False, "all available services"

