import requests
from datetime import datetime

GENDER = ""
WEIGHT_KG = 
HEIGHT_CM = 
AGE = 

APP_ID = ""
API_KEY = ""

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
sheety_endpoint = "https://api.sheety.co/eedae3a1e65a54bcf482a3f548a4aa60/myWorkouts/workouts"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}
params ={
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}


response = requests.post(url=exercise_endpoint, json=params, headers=headers)
result = response.json()

for index in range(len(result)+1):
    exercise = result["exercises"][index]["name"]
    duration = result["exercises"][index]["duration_min"]
    calories = result["exercises"][index]["nf_calories"]
    today = datetime.now()
    date_string = today.strftime("%d/%m/%Y")
    time_string = today.strftime("%H:%M:%S")
    data_for_sheet = {
        "workout": {
            "Date": date_string,
            "Time": time_string,
            "Exercise": exercise,
            "Duration": duration,
            "Calories": calories
        }
    }
    response = requests.post(url=sheety_endpoint, json=data_for_sheet)
    response.raise_for_status()
