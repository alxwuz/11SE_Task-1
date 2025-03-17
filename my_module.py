import requests
import random

api_key = "63c9ea7502f74f61a0233952251103"
base_url = "http://api.weatherapi.com/v1"

def fetch_weather(city_name):
    """
    Fetches the current weather data for a given city using WeatherAPI.
    """
    complete_url = f"{base_url}/current.json?key={api_key}&q={city_name}"
    response = requests.get(complete_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None
    
def display_weather_info(weather_data):
    """
    Displays weather information from the API response.
    """
    if weather_data:
        location = weather_data["location"]["name"]
        region = weather_data["location"]["region"]
        country = weather_data["location"]["country"]
        temperature = weather_data["current"]["temp_c"] 
        condition = weather_data["current"]["condition"]["text"]

        print(f"Weather in {location}, {region}, {country}:")
        print(f"Temperature: {temperature}°C")
        print(f"Condition: {condition}")
    else:
        print("Error retrieving weather data.")

def main():
    """
    Main function to fetch and display weather information.
    """
    city_name = input('Enter your city: ')
    weather_data = fetch_weather(city_name)
    display_weather_info(weather_data)

if __name__ == "__main__":
    main()

random = random.randint(0,5)
print(random)