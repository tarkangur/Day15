import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 184
AGE = 26

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheet_endpoint = os.environ["sheet_endpoint"]

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}
bearer_headers = {
    "Authorization": f"Bearer {os.environ["TOKEN"]}"
}

response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()

for exercise in result["exercises"]:
    today = datetime.now()
    date_string = today.strftime("%d/%m/%Y")
    time_string = today.strftime("%H:%M:%S")
    data_for_sheet = {
        "workout": {
            "date": date_string,
            "time": time_string,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_response = requests.post(url=sheet_endpoint, json=data_for_sheet, headers=bearer_headers)
    print(sheet_response.text)
