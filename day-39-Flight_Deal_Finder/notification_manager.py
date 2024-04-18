from twilio.rest import Client
import smtplib

account_sid = ""
auth_token = ""
my_email = ""
password = ""


class NotificationManager:

    def __init__(self):
        self.client = Client(account_sid, auth_token)

    def send_sms(self, message):
        message = self.client.messages \
            .create(
                body=message,
                from_='',
                to=''
            )
        print(message.sid)

    def send_emails(self, message, emails):
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
