from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager
import time, os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

options = Options()
options.headless = True

service = Service(GeckoDriverManager().install())

driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://python.org")
    driver.maximize_window()
    searchInput = driver.find_element("xpath", "/html/body/div/header/div/div[2]/div/form/fieldset/input")
    searchInput.send_keys("django")

    buttonSubmit = driver.find_element("id", "submit")
    buttonSubmit.click()

    driver.save_screenshot("python.org.1.png")
    driver.find_element("tag name", "body").screenshot("python.org.2.png")

    print("Tytuł strony to: ", driver.title)
    time.sleep(5)
finally:
    driver.quit()