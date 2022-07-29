import requests
import datetime as dt

pixela_endpoint = "https://pixe.la/v1/users"
USERNAME= "#YOUR USERNAME"
TOKEN = "# YOUR TOKEN ID"
GRAPH_ID = "graph1"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)
# {"message":"Success. Let's visit https://pixe.la/@USERNAME , it is your profile page!","isSuccess":true}

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Vishwesh workings",
    "unit": "Hours",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)
# today = dt.datetime.now()
today = dt.datetime(year=2022, month=6, day=12)
today_date = today.strftime("%Y%m%d")
print(today.strftime("%Y%m%d"))

http_method = {
    "date": today_date,
    "quantity": "1.0",
}

# post -> inserting value
http_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

# response = requests.post(url=http_endpoint, json=http_method, headers=headers)
# print(response.text)
put_method = {
    "quantity": "0.10",
}

# update -> put method
put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
# response = requests.put(url=put_endpoint, json=put_method, headers=headers)
# print(response.text)

# delete = to delete a value

delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today_date}"
response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
