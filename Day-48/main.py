from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"The price is {price_dollar.text}.{price_cents.text}")

# search_bar = driver.find_element(By.NAME, value="q")
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation_link = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation_link.text)

# bug_link = driver.find_element(By.XPATH, value='//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
# print(bug_link.text)

event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")
events = {}

for i in range(len(event_times)):
    events[i] = {
        "time": event_times[i].text,
        "name": event_names[i].text
    }

# for i in range(len(events_list)):
#     print(i)
    # print(events_list[i].find_element(By.TAG_NAME, value="li"))


# driver.close()
driver.quit()

# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[1]
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[2]
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[3]
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[4]
# //*[@id="content"]/div/section/div[2]/div[2]/div/ul/li[5]
