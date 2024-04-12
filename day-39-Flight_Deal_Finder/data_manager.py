import requests

sheet_endpoint = ""
sheet_header = {
    "Authorization": "Bearer "
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=sheet_endpoint, headers=sheet_header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_code(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheet_endpoint}/{city['id']}",
                json=new_data,
                headers=sheet_header
            )
