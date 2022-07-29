import datetime as dt
import random as r
import smtplib

g_mail = "#YOUR MAILID"
password = "#YOUR PWD"
yh_mail = "#SENDER EMAIL"


def smtp_mail(quote):
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=g_mail, password=password)
        connection.sendmail(from_addr=g_mail, to_addrs=yh_mail, msg=f"Subject:Good Morning\n\n{quote}")


def open_file():
    with open("quotes.txt", "r") as file:
        quotes_list = [line.strip() for line in file]
    smtp_mail(r.choice(quotes_list))


now = dt.datetime.now()
dow = now.weekday()
if dow == 0:
    open_file()

# day = now.day
# month = now.month
# year = now.year
# dob = dt.datetime(year=1997, month=5, day=27,hour=7, minute=25, second=30)
# print (day, "\n", month, "\n", year, "\n", dob, "\n")
# print("weekday: ", now.weekday())
