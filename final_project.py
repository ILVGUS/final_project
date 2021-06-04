# Jennifer Adams
# CIS245-T301
# June 03, 2021
# Final Project
# 
# Python program that accepts user input zip code or city and uses that input
# to obtain weather forecasts from http://openweathermap.org, then displays the 
# forecast such that it can be easily understood. The program must use functions,
# including main, must run multiple times, must validate entered data and notify
# if invalid (try blocks), and must use requests library to request webservice data.
import requests, json

# Introduction Function  
def introduce_concept():
    # Tells user program title and explains program function.
    print('''Welcome to the Weather Forecaster. The program can use city or ZIP Code input to
report current weather conditions for a given area.''')

# Function for forecasts by city.
def city_forecast():
    # My API key from openweathermap.org.
    api_key = "f48fa9237b315b1d51e5a60de57ea02f"
    starting_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # While loop for iteration
    while True:

        #Try/Except for string input of city name.
        try:
        # Collect the user's city name.
            user_city = input("\nEnter the city name that you want a forecast for: ")

            # If the entered name is not a string. . .
            if not user_city.isalpha():
                # Raise an error. . .
                raise ValueError

        # and tell the user what went wrong without showing traceback.                                   
        except ValueError:
            print("Invalid input. Please enter a city name.")

        # Otherwise, if input is a string, assign input to variable "city_name".              
        else:
            city_name = user_city.lower()
            break
               
    # Use starting URL, my API, and user-entered city name to get forecast.
    whole_city_url = starting_url + "appid=" + api_key + "&q=" + city_name

    # Try/Except for network connection.
    try:
        # Generate request and store in variable 'city_weather_data'.
        city_weather_data = requests.get(whole_city_url)
        # Assign information to a list in a format Python understands.
        whole_city_data = city_weather_data.json()

    # If no connection is made. . .
    except requests.exceptions.RequestException as error:
        # Tell the user the connection failed. . .
        print("Connection Unsuccessful.")
        # and raise an error that exits the program.
        raise SystemExit(error)
    
    # Otherwise perform the rest of the program functions.
    else:
        # Let user know the API connection succeeded.
        print("\nConnection to API Successful!")
        
        # Try the user input variable "city_name" against the API.
        try:
            # Assign portions of generated data into separate variables for each piece
            # of weather data shown.
            whole_city_stats = whole_city_data["main"]
            whole_city_conditions = whole_city_data["weather"]
            whole_city_cloudcover = whole_city_data["weather"]
            whole_city_wind = whole_city_data["wind"]      
        
            city_current_temp = whole_city_stats["temp"]
            # Use formula to convert Kelvin to Fahrenheit and assign to variable.
            city_converted_temp = (city_current_temp - 273.15) * 1.8 + 32

            city_current_feelslike = whole_city_stats["feels_like"]
            # Use formula to convert Kelvin to Fahrenheit and assign to variable.
            city_converted_feelslike = (city_current_feelslike - 273.15) * 1.8 + 32

            city_weather_determine = whole_city_conditions[0]["main"]
            city_weather_conditions = whole_city_conditions [0]["description"]
            city_current_clouds = whole_city_cloudcover [0]["description"]
            city_current_wind = whole_city_wind["speed"]

            city_current_lowtemp = whole_city_stats["temp_min"]
            # Use formula to convert Kelvin to Fahrenheit and assign to variable.
            city_converted_lowtemp = (city_current_lowtemp - 273.15) * 1.8 + 32

            city_current_hightemp = whole_city_stats["temp_max"]
            # Use formula to convert Kelvin to Fahrenheit and assign to variable.
            city_converted_hightemp = (city_current_hightemp - 273.15) * 1.8 + 32

            city_current_pressure = whole_city_stats["pressure"]
            city_current_humidity = whole_city_stats["humidity"]

        # If "city_name" is not a valid city name. . .   
        except KeyError:
            # Let user know their city is invalid and ask them to try again. . .
            print("Invalid city name. Please check your input and try again.")

        # Otherwise, perform the rest of the program steps.
        else:   
            # Print the forecast for the user.
            print("\nThe current forecast for", city_name.title(),"is as follows: \n")
            
            # If the string data in list "weather" is "Clouds". . .
            if city_weather_determine == "Clouds":
                # Assign the cloud description to "city_clouds" . . .
                city_clouds = city_current_clouds.lower()
                # and use if, elif, else statement as mock switch statement to assign a
                # cloudcover description to the data.
                if city_clouds == 'clear sky':
                    print("Cloudcover: Clear Skies")
 
                elif city_clouds == 'few clouds' or 'scattered clouds':
                    print("Cloudcover: Partly Cloudy")            
  
                elif city_clouds == 'broken clouds':
                    print("Cloudcover: Mostly Cloudy")
              
                elif city_clouds == 'overcast clouds':
                    print("Cloudcover: Overcast")                      

            # But if the string data in "weather" is not "Clouds", print what the
            # weather description says the weather should be.
            else:
                print("Weather Conditions:", city_weather_conditions.title())
            
            # Assign list data from city_current_wind to variable "city_wind". . .
            city_wind = city_current_wind
            
            # And use an if, elif, else statement as mock switch statement to assign a
            # wind description to the data.
            if city_wind <= 3.99:
                print("Wind Conditions: Calm/No Wind")           

            elif  city_wind >= 4 < 12.99:
                print("Wind Conditions: Slightly Breezy")            
      
            elif city_wind >= 13 < 24.99:
                print("Wind Conditions: Breezy")             
         
            elif city_wind >= 14 < 38.99:
                print("Wind Conditions: Windy")
        
            else:
                print("Wind Conditions: Extremely Windy")
                
            # Print the rest of the forecast data to the user, rounding to two
            # decimal places when appropriate.
            print("Current Temperature:", round(city_converted_temp,2),"F")
            print("Temperature Feels Like:", round(city_converted_feelslike,2),"F")
            print("Today's High Temperature is:", round(city_converted_hightemp,2),"F")
            print("Today's Low Temperature is:", round(city_converted_lowtemp,2),"F")
            print("Atmospheric Pressure:", city_current_pressure,"mb")
            print("Humidity:", city_current_humidity,"%")

# Function for forecasts by Zip Code.
def zip_forecast():
    # My API key from openweathermap.org.
    api_key = "f48fa9237b315b1d51e5a60de57ea02f"
    starting_url = "http://api.openweathermap.org/data/2.5/weather?"
    
    # While loop for iteration.
    while True:
    #Try/Except for integer input of ZIP code.
        try:
            # Collect the user's zip code.
            user_zip_code = int(input("\nEnter the ZIP Code of the location you want a forecast for: "))
        # If the user's input is not an integer. . .                
        except ValueError:
            # Let the user know and ask them to try again.
            print("Invalid input. Please enter a five digit ZIP code.")
        # Otherwise, format the zip code to account for leading zeros, convert it to a string,
        # and assign it to variable "zip_code".                
        else:
            zip_code = str("%05d" % user_zip_code)
            # If the user did not enter five integers. . .
            if len(zip_code) != 5:
                # Tell them to enter five integers.
                print("Invalid entry. Please enter a five digit ZIP Code.")
            # If the user entered five integers, continue with the program.                    
            else:
                break
                
    # Use starting URL, my API, and user-entered Zip Code to get forecast.
    whole_zip_url = starting_url + "appid=" + api_key + "&zip=" + zip_code
    # Try/Except for network connection.
    try:
        # Generate request and store in variable 'zip_weather_data'.
        zip_weather_data = requests.get(whole_zip_url)
        # Assign information to a list that Python can understand.
        whole_zip_data = zip_weather_data.json()
    # If the connection is not successful. . .       
    except requests.exceptions.RequestException as error:
        # Tell the user. . .
        print("Connection Unsuccessful.")
        # And raise an error that exits the program.
        raise SystemExit(error)
    # But if the connection is successful. . .
    else:
        print("\nConnection to API Successful!")       
        # Try the variable "zip_code" against the API. . .
        try:
            # Assign portions of generated data into separate variables for each piece
            # of weather data shown.
            whole_zip_cityname = whole_zip_data["name"]
            whole_zip_stats = whole_zip_data["main"]
            whole_zip_conditions = whole_zip_data["weather"]
            whole_zip_cloudcover = whole_zip_data["weather"]
            whole_zip_wind = whole_zip_data["wind"]      
        
            zip_current_temp = whole_zip_stats["temp"]
            # Use formula to convert Kelvin to Fahrenheit and assign to variable.
            zip_converted_temp = (zip_current_temp - 273.15) * 1.8 + 32

            zip_current_feelslike = whole_zip_stats["feels_like"]
            # Use formula to convert Kelvin to Fahrenheit and assign to variable.
            zip_converted_feelslike = (zip_current_feelslike - 273.15) * 1.8 + 32

            zip_weather_determine = whole_zip_conditions[0]["main"]
            zip_weather_conditions = whole_zip_conditions [0]["description"]
            zip_current_clouds = whole_zip_cloudcover [0]["description"]
            zip_current_wind = whole_zip_wind["speed"]

            zip_current_lowtemp = whole_zip_stats["temp_min"]
            # Use formula to convert Kelvin to Fahrenheit and assign to variable.
            zip_converted_lowtemp = (zip_current_lowtemp - 273.15) * 1.8 + 32

            zip_current_hightemp = whole_zip_stats["temp_max"]
            # Use formula to convert Kelvin to Fahrenheit and assign to variable.
            zip_converted_hightemp = (zip_current_hightemp - 273.15) * 1.8 + 32

            zip_current_pressure = whole_zip_stats["pressure"]
            zip_current_humidity = whole_zip_stats["humidity"]
            zip_city = whole_zip_cityname

        # If the variable "zip_code" is invalid. . .""
        except KeyError:
            # Tell the user and ask them to try again.
            print("Invalid ZIP Code entered. Please check your input and try again.")

        # Otherwise, continue with the rest of the program.
        else:
            # Print forecast information for user.
            print("\nThe current forecast for",zip_city,",",zip_code,"is as follows: \n")                 
  
            # If the string data in list "weather" is "Clouds". . .
            if zip_weather_determine == "Clouds":
                # Assign list data to variable "zip_clouds". . .
                zip_clouds = zip_current_clouds.lower()

                # and use if, elif, else statement as mock switch statement to assign a
                # cloudcover description to the data.
                if zip_clouds == 'clear sky':
                    print("Cloudcover: Clear Skies")
             
                elif zip_clouds == 'few clouds' or 'scattered clouds':
                    print("Cloudcover: Partly Cloudy")            
       
                elif zip_clouds == 'broken clouds':
                    print("Cloudcover: Mostly Cloudy")
           
                elif zip_clouds == 'overcast clouds':
                    print("Cloudcover: Overcast")                        

            # But if the string data in "weather" is not "Clouds", print what the
            # weather description says the weather should be.
            else:
                print("Weather Conditions:", zip_weather_conditions.title())
            
            # Assign list information for wind to variable "zip_wind".
            zip_wind = zip_current_wind
            
            # And use an if, elif, else statement as mock switch statement to assign a
            # wind description to the data.
            if zip_wind <= 3.99:
                print("Wind Conditions: Calm/No Wind")           

            elif  zip_wind >= 4 < 12.99:
                print("Wind Conditions: Slightly Breezy")            

            elif zip_wind >= 13 < 24.99:
                print("Wind Conditions: Breezy")             

            elif zip_wind >= 14 < 38.99:
                print("Wind Conditions: Windy")     

            else:
                print("Wind Conditions: Extremely Windy")
                
            # Print the rest of the forecast data to the user, rounding to two
            # decimal places when appropriate.
            print("Current Temperature:", round(zip_converted_temp,2),"F")
            print("Temperature Feels Like:", round(zip_converted_feelslike,2),"F")
            print("Today's High Temperature is:", round(zip_converted_hightemp,2),"F")
            print("Today's Low Temperature is:", round(zip_converted_lowtemp,2),"F")
            print("Atmospheric Pressure:", zip_current_pressure,"mb")
            print("Humidity:", zip_current_humidity,"%")
    
# Function containing program code
def main():
    # Call function introduce_concept
    introduce_concept()
    # Initialize variable for input.
    while True:
        # Ask user if they want to search by city or by zip code.
        retrieve_weather = input("\nEnter 'city' to search by city, 'zip' to search by ZIP Code, or 'quit' to quit: ")
        # If the user enters 'city'. . . 
        if retrieve_weather == 'city':
            # Call function city_forecast to display information.
            city_forecast()
        # If the user enters 'zip'. . . 
        elif retrieve_weather == 'zip':
            # Call function zip_forecast to display information.
            zip_forecast()
        # If the user enters 'quit'. . .
        elif retrieve_weather == 'quit':
            # Notify of program close. . .
            print("Exiting program.")
            # Exit loop and close program.
            break
        # If the user entered neither city nor zip. . . 
        else:
            # Notify user that their input was not valid.
            print("Invalid input. Please enter 'city' or 'zip' to begin entry.")  

# Call function main to run program.        
if __name__=="__main__":
    main()        