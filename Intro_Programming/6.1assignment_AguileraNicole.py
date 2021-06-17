# DSC 510
# 6.1 Programming Assignment
# "Temperatures" with User Input
# Nicole Aguilera
# 07/12/2020

temperature = []

looping = True
while looping == True:
    answer = input('Please input a temperature, or the word "stop" to finish inputting numbers:')
    if answer == 'stop':
        looping = False
    else:
        temperature.append(float(answer))

len_temp = len(temperature)
high_temp = max(temperature)
low_temp = min(temperature)

print("Thank you for entering", len_temp, "temperatures. The highest temperature is", high_temp,"." 
                "The lowest temperature is", low_temp,".")
