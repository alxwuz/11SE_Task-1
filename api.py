"""
Import needed modules
"""
import requests

"""
API key and url
"""
api_key = "63c9ea7502f74f61a0233952251103"
base_url = "http://api.weatherapi.com/v1"

"""
Gets the information from the API using the variables
"""
def fetch_weather(city_name):
    complete_url = f"{base_url}/current.json?key={api_key}&q={city_name}"
    response = requests.get(complete_url)
    if response.status_code == 200:
        return response.json() # If successful (code 200), returns the response
    else:
        return None # If not, doesn't do anything

"""
Formats the given data
"""
def format_weather_data(weather_data):
    if weather_data:
        location = weather_data["location"]["name"]
        region = weather_data["location"]["region"]
        country = weather_data["location"]["country"]
        temperature = weather_data["current"]["temp_c"]
        condition = weather_data["current"]["condition"]["text"]
        return (f"Weather in {location}, {region}, {country}:\n"
                f"Temperature: {temperature}°C\nCondition: {condition}") # Returns the formatted data
    else:
        return "There was an error retrieving your data from the city." # If it cannot format, it will display this
    