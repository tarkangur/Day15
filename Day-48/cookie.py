from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_option)

driver.get("https://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID, value="cookie")


timeout = 300

timeout_start = time.time()


while time.time() < timeout_start + timeout:
    cookie.click()
    curser = driver.find_element(By.CSS_SELECTOR, value="#buyCursor b")
    curser_price = curser.text.split()[-1].replace(",", "")

    grandma = driver.find_element(By.CSS_SELECTOR, value="#buyGrandma b")
    grandma_price = grandma.text.split()[-1].replace(",", "")

    factory = driver.find_element(By.CSS_SELECTOR, value="#buyFactory b")
    factory_price = factory.text.split()[-1].replace(",", "")
    mine = driver.find_element(By.CSS_SELECTOR, value="#buyMine b")
    mine_price = mine.text.split()[-1].replace(",", "")

    shipment = driver.find_element(By.CSS_SELECTOR, value="#buyShipment b")
    shipment_price = shipment.text.split()[-1].replace(",", "")

    alchemy_lab = driver.find_element(By.XPATH, value='//*[@id="buyAlchemy lab"]/b')
    alchemy_lab_price = alchemy_lab.text.split()[-1].replace(",", "")

    portal = driver.find_element(By.CSS_SELECTOR, value="#buyPortal b")
    portal_price = portal.text.split()[-1].replace(",", "")

    time_machine = driver.find_element(By.XPATH, value='//*[@id="buyTime machine"]/b')
    time_machine_price = time_machine.text.split()[-1].replace(",", "")

    money = driver.find_element(By.ID, value="money").text.replace(",", "")

    if (int(time.time()) - int(timeout_start)) % 5 == 0:
        if int(money) >= int(time_machine_price):
            time_machine.click()
        elif int(money) >= int(portal_price):
            portal.click()
        elif int(money) >= int(alchemy_lab_price):
            alchemy_lab.click()
        elif int(money) >= int(shipment_price):
            shipment.click()
        elif int(money) >= int(mine_price):
            mine.click()
        elif int(money) >= int(factory_price):
            factory.click()
        elif int(money) >= int(grandma_price):
            grandma.click()
        elif int(money) >= int(curser_price):
            curser.click()
        time.sleep(0.7)
cookies_second = driver.find_element(By.ID, value="cps")
print(cookies_second.text)
