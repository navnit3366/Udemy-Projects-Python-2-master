# Here I'm going to make an automatic Tinder Swiping Bot
# I AM NOT DOING THIS CUZ I LIKE THIS, I'M DOING THIS FOR THE COURSE ( ˘︹˘ )

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
import config

chrome_driver_path = "C:\\chrome-driver\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = Chrome(service=service)
driver.maximize_window()

URL = "https://tinder.com/"
driver.get(URL)

driver.find_element(By.XPATH, "//*[text()='Log in']").click()  # Clicking on "Log In"
print("Click on 'Continue with Google' Manually")
# Can't find out a way to automatically click on "Log In with Google", so going to do it manually
time.sleep(7)

# After clicking on "Continue with Google":
main_window = driver.window_handles[0]
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)  # Switching to login window

# Entering the email and "continue" button
driver.find_element(By.XPATH, '/html/body/div[1]/div[1]/div[2]/div/c-wiz/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div/div[1]/div/div[1]/input').send_keys(config.email)
driver.find_element(By.XPATH, '//*[@id="identifierNext"]/div/button').click()

time.sleep(20)