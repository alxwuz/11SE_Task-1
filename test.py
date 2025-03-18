import tkinter as tk
from my_module import *

def get_weather():
    city_name = city_input.get()
    weather_data = fetch_weather(city_name)
    result = format_weather_data(weather_data)
    result_label.config(text=result)

root = tk.Tk()
root.title("Alex's Weather API")
root.config(bg="lightblue")
root.geometry("300x300")

welcome_label = tk.Label(
    text="Alex's Weather Application",
    bg="lightblue",
    font=("Arial", 14, "bold")
)
welcome_label.pack(pady=10)

instructions_label = tk.Label(
    text="Enter a city and press the button to get weather information.",
    bg="lightblue",
    wraplength=280
)
instructions_label.pack(pady=5)

city_input = tk.Entry(
    font=("Arial", 12),
    justify="center"
)
city_input.pack(pady=10)

submit_button = tk.Button(
    text="Get Results",
    command=get_weather,
    bg="white",
    font=("Arial", 12, "bold")
)
submit_button.pack(pady=10)

result_label = tk.Label(
    text="",
    bg="lightblue",
    font=("Arial", 12),
    wraplength=280,
    justify="left"
)
result_label.pack(pady=10)

root.mainloop()
