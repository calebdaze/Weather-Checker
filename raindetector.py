#My libs fr
import webbrowser

import requests
from plyer import notification

#Calling ipapi and getting lat and long for the weather API
LocationRequest = requests.get("https://ipwho.is/")
locationData = LocationRequest.json()
lat = locationData['latitude']
long = locationData['longitude']

#All the openWeather API stuff
openWeatherAPIKey = 'enter key here'
weatherURL = (
    f"https://api.openweathermap.org/data/3.0/onecall?"
    f"lat={lat}&lon={long}&exclude=current,minutely,daily,alerts&units=metric&appid={openWeatherAPIKey}"
)
weatherRequest = requests.get(weatherURL)
weatherData = weatherRequest.json()

#FUNction to send the notification
def noti():
    notification.notify(
        title="Rain is coming!",
        message="Rain is expected to come within the next hour!",
        timeout=5  # seconds
    )

#Check hourly forecasts for rain
for hour in weatherData['hourly'][:1]:  #next 2 hours
    if 'rain' in hour:
        noti()
    else:
        print("Will check in a hour")

#TODO: MultiThread and sleep so it actually checks every :30 mins. Also make it in the tray. Lastly make it start on startup on PC :)
