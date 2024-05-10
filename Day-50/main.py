import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
import os

FB_EMAIL = os.environ["email"]
FB_PASSWORD = os.environ["password"]

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://tinder.com/")

time.sleep(2)
login_button = driver.find_element(By.XPATH, value='//*[@id="u605472098"]/div/div[1]/div/main/div[1]/div/div/div/'
                                                   'div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

time.sleep(2)
facebook = driver.find_element(By.XPATH, value='//*[@id="u-1122908978"]/div/div[1]/div/div[1]/div/'
                                               'div/div[2]/div[2]/span/div[2]/button')
facebook.click()

time.sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)


e_mail = driver.find_element(By.ID, value="email")
password = driver.find_element(By.ID, value="pass")
e_mail.send_keys(FB_EMAIL)
password.send_keys(FB_PASSWORD)
password.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

time.sleep(10)
allow_location = driver.find_element(By.XPATH, value='//*[@id="u-1122908978"]/div/div[1]/div/div/div[3]'
                                                     '/button[1]/div[2]/div[2]')
allow_location.click()
time.sleep(2)
notification_button = driver.find_element(By.XPATH, value='//*[@id="u-1122908978"]/div/div[1]/div/div'
                                                          '/div[3]/button[2]/div[2]/div[2]')
notification_button.click()
time.sleep(2)
cookies = driver.find_element(By.XPATH, value='//*[@id="u605472098"]/div/div[2]/div/div/div[1]'
                                              '/div[2]/button/div[2]/div[2]/div')
cookies.click()
time.sleep(2)

first_like_button = driver.find_element(By.XPATH, value='//*[@id="u605472098"]/div/div[1]/div/main'
                                                        '/div[1]/div/div/div[1]/div[1]/div/div[3]/div/div[4]/button')
first_like_button.click()

for i in range(100):

    time.sleep(1)

    try:
        like_button = driver.find_element(By.XPATH, value='//*[@id="u605472098"]/div/div[1]/div/main/div[1]'
                                                          '/div/div/div[1]/div[1]/div/div[4]/div/div[4]/button')
        like_button.click()
    except ElementClickInterceptedException:
        dismiss_button = driver.find_element(By.XPATH, value='//*[@id="u-1122908978"]/div/div/div[2]/button[2]')
        dismiss_button.click()

    except NoSuchElementException:
        time.sleep(2)
driver.quit()
