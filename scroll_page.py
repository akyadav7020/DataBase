"""
Woking fine in local but after deploying no responce, so only checking for 1st page on deplyment link.

"""


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import os
import time

def Scroll_Page(link,i):
    try:

        chrome_options = webdriver.ChromeOptions()
        chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-dev-shm-usage")
        chrome_options.add_argument("--no-sandbox")
        driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)
        driver.get(link)
        time.sleep(5)
        for k in range(i):
            x = 2000 * k + 1
            driver.execute_script("window.scrollBy(0,{})".format(x), "")
            time.sleep(3)
        html = driver.page_source
        return html
    except Exception as e:
        return e
