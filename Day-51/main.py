from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time

TW_USERNAME = os.environ["username"]
TW_PASSWORD = os.environ["password"]
PROMISED_DOWN = 150
PROMISED_UP = 10


class InternetSpeedTwitterBot:

    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_option)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)

        go_button = self.driver.find_element(By.CLASS_NAME, value="start-text")
        go_button.click()

        time.sleep(60)
        self.down = self.driver.find_element(By.CLASS_NAME, value="download-speed").text
        self.up = self.driver.find_element(By.CLASS_NAME, value="upload-speed").text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/i/flow/login")
        time.sleep(5)

        email = self.driver.find_element(By.TAG_NAME, value="input")
        email.send_keys(TW_USERNAME, Keys.ENTER)
        time.sleep(5)

        password = self.driver.find_element(By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]'
                                                            '/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label'
                                                            '/div/div[2]/div[1]/input')
        password.send_keys(TW_PASSWORD, Keys.ENTER)
        time.sleep(5)

        message = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div'
                                                           '/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div'
                                                           '/div/div/div/div/div/div/div/div/div/label/div[1]/div/div'
                                                           '/div/div/div/div[2]/div/div/div/div/span/br')
        message.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for"
                          f" {PROMISED_DOWN}down/{PROMISED_UP}up?")
        tweet_button = self.driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div[2]/main/div/div/div'
                                                                '/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]'
                                                                '/div[2]/div[2]/div/div/div/div[3]/div/span/span')
        tweet_button.click()
        time.sleep(2)
        self.driver.quit()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
