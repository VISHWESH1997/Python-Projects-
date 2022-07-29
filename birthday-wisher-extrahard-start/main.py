##################### Extra Hard Starting Project ######################

import random
import smtplib
import datetime as dt
from pandas import *

G_MAIL = "#MAILID"
PASSWORD = "#PWD"

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME]
# with the person's actual name from birthdays.csv
# 4. Send the letter generated in step 3 to that person's email address.

data = read_csv("birthdays.csv")
data_dict = data.to_dict(orient='records')
now = dt.datetime.now()
for value in data_dict:
    if value['month'] == now.month and value['day'] == now.day:
        name = value['name']
        letter = random.randint(1, 3)
        with open(f"./letter_templates/letter_{letter}.txt", 'r') as file:
            letter_list = file.read()
            letter_list = letter_list.replace('[NAME]', name)
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=G_MAIL, password=PASSWORD)
            connection.sendmail(from_addr=G_MAIL,
                                to_addrs=value['email'],
                                msg=f"Subject:Happy Birthday\n\n{letter_list}"
                                )
