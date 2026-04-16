import requests
import os
from twilio.rest import Client


OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
weather_params = {
    "lat": 52.219795,
    "lon": 21.094974,
    "appid": api_key,
    "cnt": 4
}

response = requests.get(OWM_ENDPOINT, params=weather_params)
# print(response.status_code)
response.raise_for_status()
# print(response.json())
weather_data = response.json()
# print(weather_data["list"][0]["weather"][0]["id"])

will_rain = False
for hour_data in weather_data["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember Lukas, take an ☂️",
        from_="+17758710241",
        to="+48607990246"
    )
    print(message.status)
