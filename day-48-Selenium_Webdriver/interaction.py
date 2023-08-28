from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep

service = Service(executable_path="C:\\chrome-driver\\chromedriver.exe")
driver = Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Clicking on things in a web page
total_articles_count = driver.find_element(By.XPATH, '//*[@id="articlecount"]/a[1]')
# total_articles_count.click()

# Entering text to entry fields
search_bar = driver.find_element(By.NAME, "search")
# search_bar.send_keys("Selenium")

#################################################### Challenge one ####################################################
driver.get("https://signup.heroku.com/")

first_name = driver.find_element(By.ID, "first_name")
first_name.send_keys("Damsith")

last_name = driver.find_element(By.ID, "last_name")
last_name.send_keys("Wijekoon")

email = driver.find_element(By.ID, "email")
email.send_keys("Somebody@example.com")

company = driver.find_element(By.ID, "company")
company.send_keys("No Company")

sleep(5)
driver.quit()