import requests
from bs4 import BeautifulSoup
import smtplib
import os
import lxml

url = ("https://www.amazon.com.tr/ORICO-Yerle%C5%9Ftirme-%C4%B0stasyonu-3%C3%97USB3-0-Multiport/dp/B0BN1GYZB3/"
       "ref=dealz_related_t1_d_sccl_2_6/262-9633949-7831669?pd_rd_w=Qs7RO&content-id=amzn1.sym.d86b5825-d7b2-46d5-"
       "a2b2-3cd09497b7e9&pf_rd_p=d86b5825-d7b2-46d5-a2b2-3cd09497b7e9&pf_rd_r=V2HXDSMPXTM63W579QSS&pd_rd_wg="
       "eIAjy&pd_rd_r=f7e6aeab-e41a-4582-be10-3661cba579ec&pd_rd_i=B0BN1GYZB3&th=1")
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                  "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"
}
my_email = os.environ["my_email"]
password = os.environ["password"]

response = requests.get(url=url, headers=headers)
web_site = response.text

soup = BeautifulSoup(web_site, "lxml")

price = soup.find(class_="aok-offscreen").getText().split()[0]
price_list = price.split(",")
price_as_float = float(f"{price_list[0]}.{price_list[1]}")
product_name = soup.find(id="title").getText().strip()


if price_as_float < 500:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="tarkangur13@gmail.com",
            msg=f"Subject:Amazon Price Alert!\n\n{product_name} is now {price} TL.\n{url}".encode('utf-8')
        )
