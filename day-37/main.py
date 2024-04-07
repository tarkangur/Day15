import requests
from datetime import date

today = date.today().strftime("%Y%m%d")

USERNAME = ""
TOKEN = ""

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Book Graph",
    "unit": "Page",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_endpoint = f"{graph_endpoint}/graph1"

pixel_config = {
    "date": today,
    "quantity": input("How many pages did you read today?")
}

response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)

update_endpoint = f"{pixel_endpoint}/20240404"

change_data = {
    "quantity": "32"
}
# response = requests.put(url=update_endpoint, json=change_data, headers=headers)
# print(response.text)

delete_endpoint = f"{pixel_endpoint}/20240405"

# response = requests.delete(url=delete_endpoint, headers=headers)
# print(response.text)
