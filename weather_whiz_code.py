import requests
import json
import pyttsx3

def speak(text):
    # Initialize the text-to-speech engine
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def get_weather_data(city):
    url = f"https://api.weatherapi.com/v1/current.json?key=e7011e879faf4e9e8a1103745231807&q={city}"
    try:
        r = requests.get(url)
        wdic = json.loads(r.text)
        if "error" in wdic:
            return None
        returned_city = wdic["location"]["name"]
        if city.lower() == returned_city.lower():
            temp_celsius = wdic["current"]["temp_c"]
            return temp_celsius
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
    except KeyError:
        return None
    except json.JSONDecodeError:
        return None

while True:
    city = input("Enter the name of the city (or 'q' to quit):\n")
    
    if city.lower() == 'q':
        print("Quitting the Weather Whiz!")
        break
    
    temp_celsius = get_weather_data(city)

    if temp_celsius is not None:
        # Print the temperature
        print(f"The current temperature in {city} is {temp_celsius} degrees Celsius.")

        # Speak the temperature
        speak(f"The current temperature in {city} is {temp_celsius} degrees Celsius.")
    else:
        error_msg = f"Sorry, weather data for {city} is not available or the city name is invalid."
        print(error_msg)
        speak(error_msg)

