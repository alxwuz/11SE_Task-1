import tkinter as tk
from my_module import *

def get_weather():
    city_name = city_input.get()
    weather_data = fetch_weather(city_name)
    result = format_weather_data(weather_data)
    input_result.config(text=result)
  
root = tk.Tk()
root.title("AlxWeather")
root.config(bg="lightblue")
root.minsize(300, 325)
root.maxsize(300, 325)
root.geometry("300x325")

title = tk.Label(
    text="AlxWeather",
    background="lightblue",
    font=("Arial", 20, "bold"),
    wraplength=250
)
title.pack(pady=15)

instructions = tk.Label(
    text="Enter a city in the input below to get its weather information.", 
    background="lightblue",
    font=("Arial", 12,),
    wraplength=250
)
instructions.pack(pady=5)

city_input = tk.Entry(
)
city_input.pack(pady=5)

submit_input = tk.Button(
    text="Get Results",
    command=get_weather
)
submit_input.pack(pady=5)

input_result = tk.Label(
    background=("skyblue"),   
    font=("Arial", 12),
    wraplength=250
)
input_result.pack(pady=10)

root.mainloop()