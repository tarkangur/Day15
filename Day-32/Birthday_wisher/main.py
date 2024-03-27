import datetime as dt
import pandas
import random
import smtplib


now = dt.datetime.now()
now_month = now.month
now_day = now.day

data_file = pandas.read_csv("birthdays.csv")
today_data = data_file.loc[(data_file['day'] == now_day) & (data_file['month'] == now_month)]




























##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.




