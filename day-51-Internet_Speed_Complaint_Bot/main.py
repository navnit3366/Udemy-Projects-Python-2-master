# Here I am going to make a bot that will tweet my internet speed if it is slower than the speed my internet provider agreed
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException
import config

CHROME_DRIVER_PATH = "C:\\chrome-driver\\chromedriver.exe"
SPEED_TEST_URL = "https://www.speedtest.net"


class InternetSpeedBot:

    def __init__(self):
        service = Service(executable_path=CHROME_DRIVER_PATH)
        self.driver = Chrome(service=service)
        self.driver.maximize_window()
        self.down = 60  # In mbps
        self.up = 20

    def get_internet_speed(self):
        """Fetches the internet speeds from "https://www.speedtest.net" """
        self.driver.get(SPEED_TEST_URL)
        self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a').click()  # Clicking on "Go" button
        time.sleep(50)  # Waiting for it to get the internet speed
        # Getting the download speed
        down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print(f"Download Speed: {down}")
        print(f"Upload Speed: {up}")
        return float(down), float(up)

    def tweet_at_provider(self):
        """Tweets the internet speeds got from the get_internet_speed() method"""

        download_speed, upload_speed = self.get_internet_speed()
        # Going to the twitter log in page
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

        bad_tweet = f"Hey Internet Provider, why is my internet speed {download_speed}down/{upload_speed}up when I pay " \
                    f"for {self.down}down/{self.up}up?\n(Speeds are in Mbps)"
        good_tweet = f"Hey Internet Provider, my internet speed is as it should be. Thanks for it."

        ########################## After logging in to Twitter ############################

        time.sleep(20)
        try:
            tweet_entry = self.find_tweet_entry()
        except NoSuchElementException:
            tweet_entry = self.find_tweet_entry()

        if self.down > download_speed or self.up > upload_speed:  # If current speeds are slower than the expected speeds
            tweet_entry.send_keys(bad_tweet)
        else:
            tweet_entry.send_keys(good_tweet)

        # Clicking on "Tweet" button
        self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]').click()
        time.sleep(1)

    def find_tweet_entry(self):
        """The only purpose of this method is to avoid crashing that happens when the program looks for the tweet entry"""
        entry = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/div/label/div[1]/div/div/div/div/div/div[2]/div/div/div/div')
        return entry


speed_bot = InternetSpeedBot()
speed_bot.tweet_at_provider()