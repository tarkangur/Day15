import smtplib
import datetime as dt
import random
my_email = ""
password = ""

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("quotes.txt", "r") as motivation:
        sentences = motivation.readlines()
        quotes_of_the_day = random.choice(sentences)

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:Monday Motivation\n\n{quotes_of_the_day}"
        )

# import smtplib
#
# my_email = ""
# password = ""
#
# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(
#         from_addr=my_email,
#         to_addrs="",
#         msg="Subject:Hello\n\nThis is the body of my email.")
#


# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# month = now.month
# day_of_week = now.weekday()
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=, month=, day=)
# print(date_of_birth)
