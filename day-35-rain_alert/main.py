import requests
import vonage

api_key = ""

MY_LAT = 
MY_LONG = 
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
    client = vonage.Client(key="", secret="")
    sms = vonage.Sms(client)
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": "",
            "text": "It's going to rain today. Remember to bring an ☔",
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")
