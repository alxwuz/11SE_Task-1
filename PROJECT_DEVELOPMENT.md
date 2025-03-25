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

## Data Dictionary

# Development

# Integration

# Testing and Debugging

# Installation

# Maintenance+
