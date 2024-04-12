from twilio.rest import Client

account_sid = ""
auth_token = ""


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def write_message(self, message):
        message = self.client.messages \
            .create(
                body=message,
                from_='',
                to=''
            )
