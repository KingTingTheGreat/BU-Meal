from selenium import webdriver
from bs4 import BeautifulSoup
import os
from dotenv import load_dotenv

load_dotenv()

USERNAME, PASSWORD = os.getenv('USERNAME'), os.getenv('PASSWORD')
URL = os.getenv('URL')

driver = webdriver.Chrome()

driver.get(URL)

username = driver.find_element(by='id', value='j_username')
password = driver.find_element(by='id', value='j_password')
submit_button = driver.find_element(by='name', value='_eventId_proceed')

username.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit_button.click()

# driver.get(URL)

print(driver.page_source)