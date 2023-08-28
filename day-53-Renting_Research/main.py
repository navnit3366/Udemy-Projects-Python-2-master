# This project is a capstone project for testing all of my web scraping skills including Selenium and BeautifulSoup
# I think using OOP would be a better approach for this project

from bs4 import BeautifulSoup
import requests
from selenium.webdriver import Chrome
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import config


class RentingResearch:

    def __init__(self):
        self.RENTING_WEBSITE_LINK = "https://www.zillow.com/homes/for_rent/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22west%22%3A-123.048563375%2C%22east%22%3A-121.96915663671875%2C%22south%22%3A37.39423627832906%2C%22north%22%3A38.02328490484952%7D%2C%22isMapVisible%22%3Afalse%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%7D"
        self.WEBSITE_URL = "https://www.zillow.com"
        self.FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSezQl8R8P3F726aoHg4eJp4-yjU9uYMfiiITwxZcciZ2Pfu0g/viewform?usp=sf_link"
        self.CHROME_DRIVER_PATH = "C:\\chrome-driver\\chromedriver.exe"

    def get_houses_info(self) -> tuple:
        """Fetches relevant information about rent houses from zillow.com using BeautifulSoup
        Returns fetches items in lists"""

        headers = {
            "User-Agent": config.user_agent,
            "Accept-Language": config.accept_language
        }
        response = requests.get(self.RENTING_WEBSITE_LINK, headers=headers)
        soup = BeautifulSoup(response.content, "html.parser")

        houses_ul = soup.find(id="grid-search-results").find(name="ul")
        elements = houses_ul.find_all(name="a", attrs={"class": "property-card-link", "tabindex": "0"}, recursive=True)
        links, prices, addresses = [], [], []

        for element in elements:
            link = element["href"]  # Link to the renting house
            # If there is something wrong with the link (if no https://zillow.com)
            if self.WEBSITE_URL not in link:
                link = self.WEBSITE_URL + link
            address = element.text  # Address of the house
            # Price of the house
            price = element.findAllNext(name="div")[2].findNext(name="span").text.split()[0].replace("+", '').replace("/mo", '')
            # Appending the collected information to corresponding lists
            links.append(link)
            prices.append(price)
            addresses.append(address)

        return links, prices, addresses

    def update(self, house_links: list[str], house_prices: list[str], house_addresses: list[str]):
        """Enters the collected data into a Google form using Selenium"""
        service = Service(executable_path=self.CHROME_DRIVER_PATH)
        driver = Chrome(service=service)
        driver.get(self.FORM_URL)
        time.sleep(2)

        for ind in range(len(house_addresses)):
            # Identifying the entries
            address_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
            price_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
            link_entry = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
            submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
            time.sleep(2)

            # Entering the details
            address_entry.send_keys(house_addresses[ind])
            price_entry.send_keys(house_prices[ind])
            link_entry.send_keys(house_links[ind])
            submit_button.click()
            time.sleep(2)
            driver.get(self.FORM_URL)
            time.sleep(2)



rr = RentingResearch()
links_list, prices_list, addresses_list = rr.get_houses_info()
print(links_list)
print(prices_list)
print(addresses_list)
rr.update(links_list, prices_list, addresses_list)