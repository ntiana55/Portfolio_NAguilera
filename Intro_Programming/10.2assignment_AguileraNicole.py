# DSC 510
# 10.2 Programming Assignment
# Weather Program
# Nicole Aguilera
# 08/10/2020

import requests

URL = 'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID=70eda237aaf324604bd220f0613a2db5'

print("Welcome to Openweather API.")

response = requests.get(url=URL)

print("\nStatus code is", response.status_code)

if response:
  print('Request is successful.')
else:
  print('Request returned an error.')

looping = True
while looping == True:
    answer = input('\nWould you like to lookup weather data by US City or zip code? Enter 1 for US City, 2 for zip code, or 0 if you are finished:')
    if answer == "1":
        retVal = input("Please enter the US City:")
        urlString = 'http://api.openweathermap.org/data/2.5/forecast?q=%s&units=imperial&APPID=70eda237aaf324604bd220f0613a2db5' % retVal
        response = requests.get(url=urlString)
        data = response.json()
        current_temp = data['list'][0]['main']['temp']
        high = data['list'][0]['main']['temp_max']
        low = data['list'][0]['main']['temp_min']
        pres = data['list'][0]['main']['pressure']
        humidity = data['list'][0]['main']['humidity']
        cloud_cvr = data['list'][0]['weather'][0]['description']
        print("\nCurrent Weather Conditions for", retVal, "\nCurrent Temp: %s degrees\nHigh Temp: %s degrees\nLow Temp: %s degrees\nPressure: %s hPa\nHumidity: %s percent\nCloud Cover: %s" %(current_temp, high, low, pres, humidity, cloud_cvr), "\n")
        # print(data)
    elif answer == "2":
        retVal = input("Please enter the US zip code:")
        urlString = 'http://api.openweathermap.org/data/2.5/forecast?zip=%s&units=imperial&APPID=70eda237aaf324604bd220f0613a2db5' % retVal
        response = requests.get(url=urlString)
        data = response.json()
        current_temp = data['list'][0]['main']['temp']
        high = data['list'][0]['main']['temp_max']
        low = data['list'][0]['main']['temp_min']
        pres = data['list'][0]['main']['pressure']
        humidity = data['list'][0]['main']['humidity']
        cloud_cvr = data['list'][0]['weather'][0]['description']
        print("\nCurrent Weather Conditions for", retVal, "\nCurrent Temp: %s degrees\nHigh Temp: %s degrees\nLow Temp: %s degrees\nPressure: %s hPa\nHumidity: %s percent\nCloud Cover: %s" %(current_temp, high, low, pres, humidity, cloud_cvr), "\n")
        # print(data)
    elif answer == "0":
        break
    else:
        print("That was not a valid response. Please enter 1 for US City or 2 for zip code.")

print("\nThank you for using Openweather API. Have a good day.")



