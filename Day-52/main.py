from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os


SIMILAR_ACCOUNT = "wonderful._.switzerland"
USERNAME = os.environ["username"]
PASSWORD = os.environ["password"]


class InstaFollower:
    def __init__(self):
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_option)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(3)

        inputs = self.driver.find_elements(By.TAG_NAME, value="input")
        inputs[0].send_keys(USERNAME)
        inputs[1].send_keys(PASSWORD, Keys.ENTER)

        time.sleep(8)
        save_login_prompt = self.driver.find_element(by=By.XPATH, value="//div[contains(text(), 'Şimdi değil')]")
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(4)
        notifications_prompt = self.driver.find_element(by=By.XPATH, value="// button[contains(text(), 'Şimdi Değil')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        time.sleep(4)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(4)
        followers_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        followers_pop_up = self.driver.find_element(By.XPATH, value=followers_xpath)

        for i in range(5):
            self.driver.execute_script(
                "arguments[0].scrollTop = arguments[0].scrollHeight",
                followers_pop_up)
            time.sleep(2)

    def follow(self):
        follow_buttons = []
        for i in range(2, 20):
            follow_button = self.driver.find_elements(By.XPATH, value=f"/html/body/div[6]/div[1]/div/div[2]/div/div"
                                                                      f"/div/div/div[2]/div/div/div[3]/div[1]/div"
                                                                      f"/div[{i}]/div/div/div/div[3]/div/button")[0]
            follow_buttons.append(follow_button)

        for follow in follow_buttons:
            try:
                follow.click()
                time.sleep(2)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'İptal')]")
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
