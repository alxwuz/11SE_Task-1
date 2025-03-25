import tkinter as tk
import ttkbootstrap
from my_module import *

def get_weather(event=None):
    city_name = city_input.get()
    weather_data = fetch_weather(city_name)
    result = format_weather_data(weather_data)
    input_result.config(text=result)
  
root = ttkbootstrap.Window(themename="superhero")
root.title("11SE Weather API")
root.minsize(300, 300)
root.maxsize(300, 300)
root.geometry("300x300")

title = ttkbootstrap.Label(
    text="AlxWeather",
    font=("Helvetica", 20, "bold"),
    bootstyle = "primary",
    wraplength=250
)
title.pack(pady=5)

instructions = ttkbootstrap.Label(
    text="Enter a city for the weather:", 
    font=("Helvetica", 14,),
    bootstyle = "info",
    wraplength=250
)
instructions.pack(pady=5)

city_input = ttkbootstrap.Entry(
    font=("Helvetica, 16")
)
city_input.pack(pady=10)

city_input.bind("<Return>", get_weather)

submit_input = ttkbootstrap.Button(
    text="Search",  
    command=get_weather,
    bootstyle="warning"
)
submit_input.pack()

input_result = ttkbootstrap.Label(  
    font=("Helvetica", 12),
    bootstyle="success",
    wraplength=250
)
input_result.pack(pady=10)

root.mainloop()