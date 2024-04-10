import requests
from twilio.rest import Client


class DataManager:

    sheet_endpoint = ""
    sheet_header = {
        "Authorization": ""
    }
    account_sid = ""
    auth_token = ""
    client = Client(account_sid, auth_token)

    def __init__(self):
        self.data = requests.get(url=self.sheet_endpoint, headers=self.sheet_header)

    def write_message(self):
        message = self.client.messages \
                .create(
                     body="",
                     from_='+12052360362',
                     to=''
                 )
