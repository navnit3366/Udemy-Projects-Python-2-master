# Here I'm going to make an automated program which will follow all the followers of a targeted account in Twitter
# Although in the course they're doing this with Instagram, when I try to make an Instagram account, it gets suspended

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import time
import config

CHROME_DRIVER_PATH = "C:\\chrome-driver\\chromedriver.exe"
TARGETED_ACCOUNT = "Wanindu49"


class TwitterFollower:

    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = Chrome(service=service)

    def login(self):
        """Logs in to Twitter"""
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(1)

        # Entering the email
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input').send_keys(config.EMAIL)
        time.sleep(1)
        # Clicking on "Next" button
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]').click()
        time.sleep(1)

        try:  # Trying to enter the password
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(config.PASSWORD)
        except NoSuchElementException:  # If it asks for username
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input').send_keys(config.USERNAME)
            time.sleep(2)
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div').click()  # Clicking on "Next Button"
            time.sleep(1)
            # Entering the password
            self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input').send_keys(config.PASSWORD)
        time.sleep(1)

        # Clicking on "Log In" button
        self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div').click()
        time.sleep(2)

    def find_followers_and_follow(self):
        """Finds and follows the followers of the targeted account"""

        self.driver.get(f"https://twitter.com/{TARGETED_ACCOUNT}/followers")  # Going to the page of followers
        time.sleep(2)
        follower_list = []
        ### CODE TO SCROLL IS BELOW BUT IT SEEMS AS IF IT IS NO LONGER WANTED SINCE TWITTER DOESN'T ALLOW MORE THAN 400 FOLLOWS PER DAY###
        # # Code to goto End of the Page
        # last_height = self.driver.execute_script("return document.body.scrollHeight")
        # while True:
        #     # Scroll down to bottom
        #     self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        #     # Wait to load page
        #     time.sleep(1)
        #     # Calculate new scroll height and compare with last scroll height
        #     new_height = self.driver.execute_script("return document.body.scrollHeight")
        #     if new_height == last_height:
        #         break
        #     last_height = new_height

        # Following people until the limit gets reached
        for i in range(1, 1000):
            try:
                button = self.driver.find_element(By.XPATH, f'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/section/div/div/div[{i}]/div/div/div/div/div[2]/div[1]/div[2]/div')
                button.click()
            except NoSuchElementException:
                # This would be raised if the maximum follow amount is reached
                break
            time.sleep(1)


follower = TwitterFollower()
follower.login()
follower.find_followers_and_follow()