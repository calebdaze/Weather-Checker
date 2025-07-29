# Weather Checker

Weather Checker is a lightweight Python-based system tray app that checks your local weather every 30 minutes and notifies you if rain is coming soon.  
It runs silently in the background with a tray icon and sends notifications so you never get caught in the rain!

---

## Features

- Automatically detects your location
- Checks hourly weather forecasts for rain
- Sends desktop notifications if rain is expected within the hour
- Runs quietly in the system tray with an icon
- Easy to quit via tray menu

---

## How to Use

### Download

Get the latest Windows executable from the https://github.com/calebdaze/Weather-Checker page.

### Run

Double-click `RainDetector.exe` to start the app. The tray icon will appear near your system clock.

### Quit

Right-click the tray icon and choose **Quit** to exit the app.

---

## Optional: Start Automatically on Windows Login

To have RainDetector start automatically when you log in:

1. Press `Win + R`, then enter:
%APPDATA%\Microsoft\Windows\Start Menu\Programs\Startup

yaml
Copy
Edit
2. Copy a shortcut of `RainDetector.exe` into this folder.

The app will now launch automatically every time you sign in.

---
## Getting an OpenWeather API Key

RainDetector requires an API key from [OpenWeather](https://openweathermap.org/api) to fetch weather data.

1. Sign up for a free account at [OpenWeather](https://home.openweathermap.org/users/sign_up).
2. Go to the API keys section of your account dashboard.
3. Copy your API key.

4. In the `raindetector.py` file, replace the `openWeatherAPIKey` variable with your own key (Line 27):

```python
openWeatherAPIKey = 'YOUR_API_KEY_HERE'
```
## License

MIT License © 2025 Caleb Daze

---

## Contributions & Feedback

Feel free to open issues or submit pull requests to improve Weather Checker!

---
