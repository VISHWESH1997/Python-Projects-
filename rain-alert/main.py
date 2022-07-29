import requests
import smtplib
API_KEY = "#YOURAPIKEY"
MY_LAT = 17.398222 # Your latitude
MY_LONG = 78.503385 # Your longitude
G_MAIL = "#Your mail ID"
PASSWORD = "#YOUR PASSWORD"

parameters = {
    'lat': 38.251968,
    'lon': 140.886215,
    'appid': API_KEY,
    'exclude': "current,minutely,daily,alerts"
}
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
data_slice = data['hourly'][:12]

is_raining = False
for hour_data in data_slice:
    cond_codes = hour_data['weather'][0]['id']
    # print(type(cond_codes))
    if cond_codes < 700:
        is_raining = True

if is_raining:
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=G_MAIL, password=PASSWORD)
        connection.sendmail(from_addr="vishweshex@gmail.com",
                            to_addrs=G_MAIL,
                            msg="Subject:raining\n\n Hey,\n It is raining out bring an Umbrella")
