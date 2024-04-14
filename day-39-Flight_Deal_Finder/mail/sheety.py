import os
import requests

sheet_endpoint = ""
sheet_token = ""


def post_new_row(name, lastname, email):
  params = {"user": {"firstName": name, "lastName": lastname, "email": email}}
  header = {"Authorization": f"Bearer {sheet_token}"}
  response = requests.post(url=sheet_endpoint, headers=header, json=params)
  response.raise_for_status
  print(response.text)
