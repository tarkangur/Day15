import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_API_KEY = ""
NEWS_API_KEY = ""
TWILIO_SID = ""
TWILIO_AUTH_TOKEN = ""


stock_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "interval": "60min",
    "apikey": STOCK_API_KEY,
    "extended_hours": "false"
}
r = requests.get(url=STOCK_ENDPOINT, params=stock_parameters)
stock_data = r.json()
stock_data_list = [value for (key, value) in stock_data.items()]

yesterday_data = stock_data_list[0]
day_before_yesterday_data = stock_data_list[1]

yesterday_close_price = float(yesterday_data["4. close"])
day_before_yesterday_close_price = float(day_before_yesterday_data["4. close"])
difference = (yesterday_close_price - day_before_yesterday_close_price)
up_down = None
if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = difference / yesterday_close_price * 100


news_parameters = {
    "qinTitle": COMPANY_NAME,
    "apiKey": NEWS_API_KEY
}
response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
news_data = response.json()
news_data_list = news_data["articles"][:3]


client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
for i in range(3):
    headline = news_data_list[i]["title"]
    brief = news_data_list[i]["description"]
    message = client.messages \
                    .create(
                        body=f"{STOCK}: {up_down}{diff_percent:.2f}%\nHeadline:{headline}\nBrief:{brief}",
                        from_='+12052360362',
                        to='+905054506333'
                     )
