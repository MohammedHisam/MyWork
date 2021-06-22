import requests
# import os
from datetime import datetime

api_key = 'a8fb18ee726f1daa6299385175aa11d4'
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

# Making a get request
response = requests.get(complete_api_link)

# checking response . if response == 404 ,entered city name not a city name
if response.status_code == 404:

    # print response
    print(response)

    # print request status_code
    print(response.status_code)

    print("Entered city name not a city name !")

else:

    # create variables to store and display data
    temp_city = ((api_data['main']['temp']) - 273.15)
    weather_desc = api_data['weather'][0]['description']
    hmdt = api_data['main']['humidity']
    wind_spd = api_data['wind']['speed']

    date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

    # making a weather.txt file and redirect print output
    w_file = open('weather.txt', 'w')

    # redirecting print output in to weather.tx file
    print("-------------------------------------------------------------", file=w_file)
    print("Weather Stats for - {}  || {}".format(location.upper(), date_time), file=w_file)
    print("-------------------------------------------------------------", file=w_file)

    print("Current temperature is: {:.2f} deg C".format(temp_city), file=w_file)
    print("Current weather desc  :", weather_desc, file=w_file)
    print("Current Humidity      :", hmdt, '%', file=w_file)
    print("Current wind speed    :", wind_spd, 'kmph', file=w_file)

    print("'weather.txt' file has been created.... \n weather details wrote successfully....")
