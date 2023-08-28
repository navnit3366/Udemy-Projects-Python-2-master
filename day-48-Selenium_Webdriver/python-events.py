# This is the first challenge using Selenium
# Here I am going to get information about upcoming python events and print it out in a dict

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

URL = "https://www.python.org/"
CHROME_DRIVER = "C:\\chrome-driver\\chromedriver.exe"

service = Service(executable_path=CHROME_DRIVER)
driver = webdriver.Chrome(service=service)
driver.get(URL)

event_dict = {}
for i in range(1, 6):
    event_date = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/time').get_attribute("datetime").split("T")[0]
    event_name = driver.find_element(By.XPATH, f'//*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[{i}]/a').text
    event_dict.update({i-1: {"date": event_date, "name": event_name}})

print(event_dict)

driver.quit()