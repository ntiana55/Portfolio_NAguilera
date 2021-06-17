# DSC 510
# 9.1 Programming Assignment
# Web Services - Chuck Norris Jokes
# Nicole Aguilera
# 08/02/2020

import requests

URL = "https://api.chucknorris.io/jokes/random"

print("Welcome to the Chuck Norris joke generator.")

looping = True
while looping == True:
    answer = input('Would you like to receive a Chuck Norris joke?')
    r = requests.get(url = URL)
    data = r.json()
    if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes":
        print("Your joke is:", data['value'])
    elif answer == "N" or answer == "n" or answer == "No" or answer == "no":
        break
    else:
        print("That was not a valid response. Please enter yes or no.")

print("Thank you for using the Chuck Norris joke generator.")
