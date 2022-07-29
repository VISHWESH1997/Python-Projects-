import requests
from datetime import datetime

APP_ID = "#YOUR APPID"
API_KEY = "#YOUR API KEY"
today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
today_time = today.strftime("%X")
print(today_time)

sheet_header = {
    "Authorization": "Bearer #USERNAME",
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

sheety_endpoint = "https://api.sheety.co/6e9c14a5d15ea63fc4319b12e1268a30/workoutsTracking/workouts"
workout_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise = str(input("What exercise did you do today: "))
print(exercise)

workout_method = {
 "query": exercise,
 "gender": "male",
 "weight_kg": 87.5,
 "height_cm": 185.92,
 "age": #YOUR AGE IN int,
}

response = requests.post(url=workout_endpoint, json=workout_method, headers=headers)
data = response.json()["exercises"]
for i in range(len(data)):
    data_exc_name = data[i]["name"]
    data_calorie = data[i]['nf_calories']
    data_time = data[i]['duration_min']
    print(i, "\n", data_exc_name, "\n", data_calorie, "\n", data_time)
    workout_items = {
        "workout": {
            'date': today_date,
            'time': today_time,
            'exercise': data_exc_name.title(),
            'duration': data_time,
            'calories': data_calorie
                }
            }
    sheety_res = requests.post(url=sheety_endpoint, json=workout_items, headers=sheet_header)
    print(sheety_res.text)







# time_str = str(data_time).split('.')
    # time_dur = datetime(year=2022, month=5, day=27, minute=int(time_str[0]), second=int(time_str[1]))
    # my_dur = time_dur.strftime("%M:%S:00")
    # print(my_dur)
