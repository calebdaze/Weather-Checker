#My libs fr
import os
import threading
import time
import webbrowser

import requests
from PIL import Image
from plyer import notification
from pystray import Icon, Menu, MenuItem

#Calling ipapi and getting lat and long for the weather API
LocationRequest = requests.get("https://ipwho.is/")
locationData = LocationRequest.json()
lat = locationData['latitude']
long = locationData['longitude']

#FUNction to send the notification
def noti():
    notification.notify(
        title="Rain is coming!",
        message="Rain is expected to come within the next hour!",
        timeout=5  # seconds
    )

#All the openWeather API stuff
openWeatherAPIKey = 'openWeatherAPIKey'
weatherURL = (
    f"https://api.openweathermap.org/data/3.0/onecall?"
    f"lat={lat}&lon={long}&exclude=current,minutely,daily,alerts&units=metric&appid={openWeatherAPIKey}"
)

def weatherLoop():
    while True:
        print("El stupido 1")
        weatherRequest = requests.get(weatherURL)
        weatherData = weatherRequest.json()
        #Check hourly forecasts for rain
        for hour in weatherData['hourly'][:1]:  #next 2 hours
            print("El Stupido 2")
            if 'rain' in hour:
                noti()
            else:
                print("Will check in a hour")
        time.sleep(1800)


#To whoever made threads I love you but PLEASEEEEEE make the documentation easier to understand geeksforgeeks is the goat
weatherThread = threading.Thread(target=weatherLoop,daemon=True)
weatherThread.start()
#icon for the weather on tray.
def quitAction(icon, item):
    print("Stopping the code!")
    icon.stop()
#Places it in a path so it can find it no matter what
iconDir = os.path.dirname(os.path.abspath(__file__))
iconPath = os.path.join(iconDir, 'heavy-rain.ico')
heavyRain = Image.open(iconPath)
icon = Icon(name="RainCloud",icon=heavyRain,title="RainDetector",menu=Menu(MenuItem("Quit", quitAction)))
#Starts the icon keeping script alive mainly the daemon (or something like that)
icon.run()
