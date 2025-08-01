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

#FUNction to send the notification, made the message customize
def noti(message):
    notification.notify(
        title="Rain is coming!",
        message=message,
        timeout=5  # seconds
    )

#All the openWeather API stuff
openWeatherAPIKey = 'YOUR_API_KEY_HERE'
weatherURL = (
    f"https://api.openweathermap.org/data/3.0/onecall?"
    f"lat={lat}&lon={long}&exclude=current,minutely,daily,alerts&units=metric&appid={openWeatherAPIKey}"
)

#I had to redo cause I didn't read the doc :(
def weatherLoop():
    while True:
        print("El stupido 1")
        weatherRequest = requests.get(weatherURL)
        weatherData = weatherRequest.json()
        print(weatherData)
        for hour in weatherData['hourly'][:2]:  # Next 2 hours
            print("El Stupido 2")
            rain = hour.get('rain', {}).get('1h', 0)
            pop = hour.get('pop', 0)
            if rain > 0:
                noti(f"Rain expected soon (~{rain} mm)!")
                break #The break helps with spam, Source: My ear drums
            elif pop >= 0.6:
                noti(f"{int(pop*100)}% chance of rain in the next hour.")
                break
            else:
                print("No rain. Will check again in 30 mins.")
        time.sleep(1800)  # Wait 30 mins
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
