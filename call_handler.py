import time
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

# Initialize WebDriver with Firefox (Headless Mode)
options = webdriver.FirefoxOptions()
options.add_argument("--headless")
service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(service=service, options=options)

# Free calling websites
CALLING_SITES = [
    "https://globfone.com/call-phone/",
    "https://www.poptox.com/",
    "https://www.citrus.tel/",
    "https://www.voipdiscount.com/",
    "https://www.dingtone.me/"
]

def make_call(phone_number):
    for site in CALLING_SITES:
        driver.get(site)
        time.sleep(5)

        try:
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

            time.sleep(10)
            return True, f"✅ Call in progress to {phone_number} using {site}"
        except:
            continue  # Try next website if one fails

    return False, "❌ Call failed using all available services."

