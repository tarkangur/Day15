import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords="
           "python%20developer&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

login = driver.find_element(By.LINK_TEXT, value="Oturum aç")
time.sleep(5)
login.click()

time.sleep(5)
username = driver.find_element(By.ID, value="username")
username.send_keys("")

password = driver.find_element(By.ID, value="password")
password.send_keys("")
password.send_keys(Keys.ENTER)


time.sleep(10)
job_list = driver.find_elements(By.CSS_SELECTOR, value=".jobs-search-results__list-item")

for job in job_list:
    job.click()
    time.sleep(2)
    easy_apply = driver.find_element(By.CSS_SELECTOR, ".jobs-apply-button--top-card button")
    easy_apply.click()
    phone = driver.find_element(By.CLASS_NAME, value="artdeco-text-input--input")
    if phone.text == "":
        phone.send_keys("")
    submit_button = driver.find_element(By.CSS_SELECTOR, value=".display-flex button")
    submit_button.click()
    time.sleep(2)
    submit_button = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
    submit_button.click()
    next_button = driver.find_elements(By.CLASS_NAME, value="artdeco-button__text")
    if next_button[2].text == "İncele":
        close_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()
        discard_button = driver.find_element(By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")
        discard_button.click()
        print("No application button, skipped.")
    else:
        finish_button = driver.find_element(By.CLASS_NAME, value="artdeco-button--primary")
        finish_button.click()
        print("Submitting job application")

time.sleep(5)
driver.quit()
