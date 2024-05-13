import time
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By


url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

links = soup.find_all(name="a", class_="StyledPropertyCardDataArea-anchor")
all_link = [link['href'] for link in links]

prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
all_prices = [prices.getText().strip("/mo").split("+")[0] for prices in prices]

addresses = soup.find_all(name="address")
all_addresses = [address.getText().strip().split("|")[-1] for address in addresses]


chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_option)

form = "https://docs.google.com/forms/d/e/1FAIpQLScNXMduTor_Shmzuspd2nbHKivWehtYRFPKEMDSVnExysgbiw/viewform"
driver.get(form)

for i in range(len(links)):
    time.sleep(1)
    address_answer = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div'
                                                         '/div[2]/div/div[1]/div/div[1]/input')
    price_answer = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div'
                                                       '/div[2]/div/div[1]/div/div[1]/input')
    link_answer = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div'
                                                      '/div[2]/div/div[1]/div/div[1]/input')

    address_answer.send_keys(all_addresses[i])
    price_answer.send_keys(all_prices[i])
    link_answer.send_keys(all_link[i])
    driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span').click()
    driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a').click()
