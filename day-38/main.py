import requests
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 184
AGE = 26

APP_ID = "e210ba46"
API_KEY = "0d4be2888187361f905c94dc36a90a01"

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/eedae3a1e65a54bcf482a3f548a4aa60/myWorkouts/workouts"

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


response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()
print(len(result))
print(result)

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
    sheet_response = requests.post(url=sheety_endpoint, json=data_for_sheet)
    print(sheet_response.text)
