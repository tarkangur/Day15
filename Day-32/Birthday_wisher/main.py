import datetime as dt
import pandas
import random
import smtplib

EMAIL = "d41913970@gmail.com"
PASSWORD = "phbasfovtikzwyds"

now = dt.datetime.now()
now_month = now.month
now_day = now.day

data_file = pandas.read_csv("birthdays.csv")
today_data = data_file.loc[(data_file['day'] == now_day) & (data_file['month'] == now_month)]
emails = [mail for mail in today_data["email"]]
names = [name for name in today_data["name"]]
for person in names:
    index = names.index(person)
    email = emails[index]
    number = random.randint(1, 3)
    with open(f"letter_templates/letter_{number}.txt", "r") as start_letter:
        letter = start_letter.read()
        final_letter = letter.replace("[NAME]", f"{person}")

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user=EMAIL, password=PASSWORD)
        connection.sendmail(from_addr=EMAIL,
                            to_addrs={email},
                            msg=f"Subject:Happy Birthday\n\n{final_letter}"
                            )
