from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "C:\\chrome-driver\\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)

driver.get("https://www.python.org/doc/")

# Finding a html element by class (You can also find by attributes, tag name, id, etc
by_class = driver.find_element(By.CLASS_NAME, "donate-button")
print(by_class.text)

# Getting a size of an image in a webpage
image = driver.find_element(By.CLASS_NAME, "python-logo")
print(image.size)

# Finding a html element with xpath (This is so easy)
copyright_text = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/div/p/small/span[1]')
print(copyright_text.tag_name) # Getting the tag name of it

# Above we always used find_element(), we can find all the elements with find_elements()

driver.quit()
