"""
Imports needed modules
"""
import tkinter as tk
import ttkbootstrap
from api import *

"""
Fetches the weather from the other python file and displays it
"""
def get_weather(event=None):
    city_name = city_input.get()
    weather_data = fetch_weather(city_name)
    result = format_weather_data(weather_data)
    input_result.config(text=result)

"""
Closes the program
"""
def exit():
    root.destroy()
  
"""
Creates the main window
"""
root = ttkbootstrap.Window(themename="superhero") # Theme of the GUI
root.title("11SE Weather API") 
root.minsize(300, 350) # Window Sizes
root.maxsize(300, 350)
root.geometry("300x350")

"""
Adds the title of the program
"""
title = ttkbootstrap.Label(
    text="AlxWeather",
    font=("Helvetica", 20, "bold"),
    bootstyle = "primary",
    wraplength=250
)
title.pack(pady=5)

"""
Adds the instructions
"""
instructions = ttkbootstrap.Label(
    text="Enter a city for the weather:", 
    font=("Helvetica", 14,),
    bootstyle = "info",
    wraplength=250
)
instructions.pack(pady=5)

"""
Adds a text box for city input
"""
city_input = ttkbootstrap.Entry(
    font=("Helvetica, 16")
)
city_input.pack(pady=10)

"""
Binds the enter key to the get_weather function
"""
city_input.bind("<Return>", get_weather)

"""
Adds a button the submit the city
"""
submit_input = ttkbootstrap.Button(
    text="Search",  
    command=get_weather,
    bootstyle="outline button"
)
submit_input.pack()

"""
Displays the weather info after submitted
"""
input_result = ttkbootstrap.Label(  
    font=("Helvetica", 12),
    bootstyle="success",
    wraplength=250
)
input_result.pack(pady=25)

"""
Exits the program when pressed
"""
exit_button =ttkbootstrap.Button(
    text="Exit Program",
    command=exit,
    bootstyle="danger"
)
exit_button.pack(pady=10, side="bottom")

"""
Loops the program until closed
"""
root.mainloop()