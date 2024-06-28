import requests
import random

def get_weather(city, api_key):
    
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"

    # API request
    response = requests.get(url)
    data = response.json()

    
    if response.status_code == 200:
        weather_description = data['current']['condition']['text'].lower()
        temperature = data['current']['temp_c']
        return weather_description, temperature
    else:
        return None, None

def suggest_clothing(weather_description, temperature):
    
    cold_clothing = ["Warm Jacket", "Sweater", "Scarf", "Beanie", "Gloves"]
    warm_clothing = ["T-shirt", "Shorts", "Sunglasses", "Cap", "Flip-flops"]
    rainy_clothing = ["Raincoat", "Umbrella", "Waterproof Boots", "Poncho"]
    moderate_clothing = ["Long Sleeve Shirt", "Jeans", "Light Jacket", "Sneakers"]

   
    if "snow" in weather_description or temperature < 10:
        clothing_suggestion = random.choice(cold_clothing)
    elif "sunny" in weather_description or temperature > 25:
        clothing_suggestion = random.choice(warm_clothing)
    elif "rain" in weather_description or "drizzle" in weather_description or "thunderstorm" in weather_description:
        clothing_suggestion = random.choice(rainy_clothing)
    else:
        clothing_suggestion = random.choice(moderate_clothing)

    return clothing_suggestion


user_city = input("Enter your city name: ")
api_key = "d2e4569533204f839ce174502242806"  

weather_description, temperature = get_weather(user_city, api_key)

if weather_description and temperature is not None:
    clothing = suggest_clothing(weather_description, temperature)
    print(f"In {user_city}, the weather is {weather_description} with a temperature of {temperature}°C. You should wear: {clothing}")
else:
    print("Please check the city name and try again.")
