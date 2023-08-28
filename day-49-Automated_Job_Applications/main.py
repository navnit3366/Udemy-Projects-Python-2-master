### OK I OFFICIALLY GIVE THIS UP

# Here I am going to make a program which checks for job applications on LinkedIn, save them and follow the companies who have posted job applications
# In the course, they recommend to actually apply to jobs, but since I can't do that, this is what I'm going to be doing

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import config

URL = "https://www.linkedin.com/jobs/search/?currentJobId=3600710880&f_AL=true&f_WT=2&geoId=100446352&keywords=python%20developer&location=Sri%20Lanka&refresh=true"
chrome_driver_path = "C:\\chrome-driver\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = Chrome(service=service)

driver.get("https://www.linkedin.com/home")

driver.find_element(By.ID, "session_key").send_keys(config.email)  # Entering the e-mail
driver.find_element(By.ID, "session_password").send_keys(config.password)  # Entering the password
driver.find_element(By.XPATH, '//*[@id="main-content"]/section[1]/div/div/form/div[2]/button').click()  # Clicking on sign-in button
# driver.find_element(By.XPATH, '//*[@id="ember459"]/button').click() In case of phone number verification

driver.get(URL)
first_job_id = 176  # It seems as if those ids are changing daily or weekly
first_follow_id = 256

driver.find_element(By.XPATH, '//*[@id="ember114"]').click()  # Hiding the chat-panel
driver.find_element(By.XPATH, f'//*[@id="ember{first_job_id}"]').click()  # Clicking on the job application
driver.find_element(By.XPATH, '//*[@id="main"]/div/div[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button').click()  # Clicking on "save" button
driver.find_element(By.XPATH, f'//*[@id="{first_follow_id}"]/section/div[1]/div[1]/button').click()  # Following the company, who posted the job application

time.sleep(10)