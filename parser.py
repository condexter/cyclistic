import requests
from bs4 import BeautifulSoup
from requests import get

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


driver = webdriver.Chrome(executable_path='/home/condexter/Desktop/chromedriver')
link = "https://divvy-tripdata.s3.amazonaws.com/index.html"

driver.implicitly_wait(10)
driver.get(link)
driver.find_elements(By.XPATH, "//*[contains(text(), 'divvy-tripdata')]")

page_source = driver.page_source

soup = BeautifulSoup(page_source, "lxml")

d_link = soup.findAll('a')
for link in d_link[::]:
    url = link['href']
    file_name = url.split('/')[-1]
    r = requests.get(url)
    open('archives/{}'.format(file_name), 'wb').write(r.content)
    print("Downloaded: ", file_name)

#file = open('selenium_code_with_wait.txt', mode='w', encoding='utf-8')
#file.write(soup.prettify())

