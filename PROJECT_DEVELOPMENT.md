# **11SE Task 1 2025 - ??? Application**
## Designed and Documented by Alex Wu
This is where all the documentation and development will occur.
# Requirements Definition
## Funtional Requirements
- **Data Retrieval:** What does the user need to be able to view in the system? 

The user must view the data that is obtained from the dataset. If there are any errors due to not having any data or something else, there will need to specify if there isn't any data or not. For example, if a movie in a dataset did not have the time of release, then it should say something like N/A, and not an error so the user knows the information is unavailable.

- **User Interface:**
What is required for the user to interact with the system?

For the user to interact with the system, the requirement will need to be a command-line interface which allows the user to understand what is happening, and use the application to connect with the API without any bugs or problems. The program will also need to be able to sort and configure the dataset for some sections of the info, such as showing the descending order from a chosen category.

- **Data Display:** What information does the user need to obtain from the system?

The user needs to be able to access all of the data from the chosen API. There cannot be any modifications of the dataset, and errors need to be

## Non-Functional Requirements
- **Performance:** How well does the system need to perform? 

The sytem needs to be fairly efficient as it cannot be too slow and perform the sorting slowly. This isn't really hard as python is a fairly fast programming language, and with the help of other modules, it won't lack in performace.

- **Reliability:** How reliable does the system and data need to be?

To have a reliable program, there needs to be a well-written application that has no bugs and can be used without breaking. There also needs to be a well chosen API, as an unreliable and innacurate API will result in a lot of errors and bugs. Preferably, the API can be chosen from https://github.com/public-apis/public-apis, as it includes a list of good public APIs that can be used for different applications.

- **Usability and Accessibility:** How easy to navigate does the system need to be? What instructions will we need for users to access the system?

There should be a README file where users can open it and get instructions on how to use the application, how to install the required repositories, etc. 

# Determining Specifications
## Functional Specifications

- **User Requirements**

The user needs to be able to view the data from the API. There will be an input, where the user can enter whatever city they like. If the data matches, it will display the weather info, and if it doesn't, it will return an error.

- **Inputs & Outputs**

It needs to accept the input city from the user and out the weather conditions in that city, including the temperature and condition.

- **Core Features**

The program must communicate with the API and get its data.

- **User Interaction**

The program will be a fairly simple application, in which it will provide the data for the user, which will then be programmed within a GUI for the user to view.

- **Error Handling**

The most common error will probably be when the data isn't found, it could be due to the API not having that data or the user entering the incorrect details. This could be handled with a prompt saying "You may have entered the incorrect prompt or the API does not have this data. Please try again.", which handles the error well and lets the user know something wrong happened.

## Non-Functional Specifications

- **Performance**

The system will need to be able to run calculations within the API efficiently, so the user does not have to wait for it for a long time. 

- **Useability / Accessibility**

To make the GUI more usable and accessible, there could be new features added such as voice to text, or a high contrast option for some people.

- **Reliability**

There won't be many program-breaking bugs or issues, as all it is programmed to do is just to fetch the data from the API based on the user's input and then displaying it. The data won't be a problem as it is just the weather, and duplicate data won't be happening in a weather program, as the old data is removed as new data is updated.

## Use Cases
- **Actor:**

User (Someone wanting to know what the weather is like in a certain city.)

- **Preconditions:** 

Internet access; API with weather data.

- **Main Flow:**

1. **Enter City** - User inputs a city that they want to know what the weather is.

2. **API Communication** – Program tells the API to retrieve the data from the specified city, which it then returns with data, or an error.

3. **Output Display** – System displays the data, if there is an error, it will tell them.

4. **New City** – If the user enters another city in the same input, the program will repeat the steps.

- **Postconditions:**

Weather data is retrieved successfully or is returned an error.

# Design
## Gantt Chart
![Alt text](images/gantt%20chart.png)

## Structure Chart
![Alt text](images/structure%20chart.png)

## Algorithms
### Main Process
![Alt text](images/algorithm.png)

#### Psuedocode
```
BEGIN root.mainloop()
INPUT city_input
IF API Request Valid THEN
    Find Weather in City
ELSE
    DISPLAY "There was an error retrieving your data from the city."    
ENDIF
END root.mainloop()
```

### get_weather
![Alt text](images/algorithm_get_weather.png)

#### Psuedocode
```
BEGIN get_weather()
    city_name = city_input.get()
    weather_data = fetch_weather(city_name)
    result = format_weather_data(weather_data)
    input_result.config(text=result)
END get_weather
```

### exit
![Alt text](images/algorithm_exit.png)

#### Psuedocode
```
BEGIN exit()
    root.destroy()
END exit()
```

## Data Dictionary
![Alt text](images/data_dictionary.png)

# Development
main.py
```
"""
Import needed modules
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
root = ttkbootstrap.Window(themename="superhero")
root.title("11SE Weather API")
root.minsize(300, 350)
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
```

api.py
```
"""
Import needed modules
"""
import requests

"""
# API key and url
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
    
```
# Integration

# Testing and Debugging

# Installation

# Maintenance
