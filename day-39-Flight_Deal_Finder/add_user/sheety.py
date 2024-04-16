import os
import requests

sheet_id = os.getenv("sheet_id")
sheet_token = os.getenv("sheet_token")
sheet_endpoint = f"https://api.sheety.co/{sheet_id}/flightDeals/users"


def post_new_row(name, lastname, email):
  params = {"user": {"firstName": name, "lastName": lastname, "email": email}}
  header = {"Authorization": f"Bearer {sheet_token}"}
  response = requests.post(url=sheet_endpoint, headers=header, json=params)
  response.raise_for_status
  print(response.text)
