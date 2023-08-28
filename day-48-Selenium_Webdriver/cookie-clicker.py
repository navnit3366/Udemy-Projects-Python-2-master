# Here I am going to "hack" a clicking game with Selenium

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time

chrome_driver = "C:\\chrome-driver\\chromedriver.exe"
URL = "https://orteil.dashnet.org/experiments/cookie/"
service = Service(executable_path=chrome_driver)
driver = Chrome(service=service)

driver.get(URL)

button = driver.find_element(By.ID, "cookie")

upgrades = driver.find_elements(By.CSS_SELECTOR, "#store div")
upgrades_ids = [i.get_attribute("id") for i in upgrades]

timeout = time.time() + 10  # 10 seconds
five_min = time.time() + 60 * 5  # 5minutes


# Game loop
while True:
    # Clicking
    button.click()
    # check the right-hand pane to see which upgrades are affordable and purchase the most expensive one.
    # You'll need to check how much money (cookies) you have against the price of each upgrade.
    if time.time() > timeout:
        current_money = int(driver.find_element(By.ID, "money").text.replace(",", ""))  # Turning into an int
        # print(current_money)
        all_prices = driver.find_elements(By.CSS_SELECTOR, "#store b")
        # for price in all_prices:
        #     print(price.text)

        prices_in_int = []
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                prices_in_int.append(cost)

        upgrades_dict = {}
        for i in range(len(prices_in_int)):
            upgrades_dict[upgrades_ids[i]] = prices_in_int[i]

        # Finding the affordable upgrades
        affordable_upgrades = {}
        for id, cost in upgrades_dict.items():
            if cost <= current_money:
                affordable_upgrades[cost] = id

        # Finding the maximum affordable upgrade
        maximum_upgrade = max(affordable_upgrades.keys())
        maximum_upgrade_id = affordable_upgrades[maximum_upgrade]

        # Purchasing it
        driver.find_element(By.ID, maximum_upgrade_id).click()

        timeout += 10
        time.sleep(0.5)  # In order to avoid crashing

    # After 5 minutes have passed since starting the game, stop the bot and print the "cookies/second"
    if time.time() > five_min:
        cookies_per_second = driver.find_element(By.ID, "cps").text
        break

print(cookies_per_second)
driver.quit()