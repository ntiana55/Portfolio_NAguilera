# DSC 510
# 5.1 Programming Assignment
# "Calculation Loops" with User Input
# Nicole Aguilera
# 07/05/2020

def performCalculation (theOperation):
    num1 = float(input('Please enter a number:'))
    num2 = float(input('Please enter a second number:'))
    if theOperation == "+" :
        Result = num1 + num2
    elif theOperation == "-":
        Result = num1 - num2
    elif theOperation == "*":
        Result = num1 * num2
    elif theOperation == "/":
        Result = num1 / num2
    else:
        print("Please enter the sign of a mathematical operation")
    print(Result)

def calculateAverage ():
    NumInput = int(input('How many numbers do you wish to input?'))
    total = 0.0
    for i in range(NumInput):
        userNumber = float(input('Please enter a number:'))
        total = total + userNumber
        print(total)
    average = total / NumInput
    print(average, "is the average of the numbers that you have inputted.")


looping = True
while looping == True:
    answer = input('Would you like to perform a calculation, an average, or are your calculations complete?')
    if answer == 'calculation':
        theOperation = input('Please enter a mathematical operation to perform:')
        if theOperation == "+" or theOperation == "-" or theOperation == "*" or theOperation == "/":
            performCalculation(theOperation)
        else:
            print("That was not a valid mathematical operation.")
    elif answer == 'average':
        calculateAverage()
    elif answer == 'complete':
        looping = False
    else:
        print("Please enter 'calculation' or 'average'. Please enter 'complete' if you are finished.")
print("Thank you for performing these calculations.")

