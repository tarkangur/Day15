import requests
from twilio.rest import Client

api_key = ""
account_sid = ""
auth_token = ""

MY_LAT = ""
MY_LONG = ""
parameters = {
        "lat": MY_LAT,
        "lon": MY_LONG,
        "appid": "",
        "cnt": 4
    }
response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
weather_data = response.json()
weather_id = [weather_data["list"][i]["weather"][0]["id"] for i in range(4)]
umbrella = 0
for number in weather_id:
    if number < 700:
        umbrella += 1
if umbrella > 0:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔",
            from_="",
            to=""
        )
    print(message.status)
