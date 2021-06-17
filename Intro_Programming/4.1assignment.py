# DSC 510
# 4.1 Programming Assignment
# Functions with User Input
# Nicole Aguilera
# 06/28/2020

print("Welcome to the Fiber Optic Calculator") # Welcome message to the user
Cname = input('Please enter the name of your company: ') # Receive company name
FOC_installed = int(input('Please enter the number of feet of fiber optic cable to be installed: '))
    # Received number of feet of cable to be installed for user
def calcCost (FOC_installed, PPF):      # Defining the function for determining the cost of cable depending on footage
    return FOC_installed * PPF

if FOC_installed > 100:                 # If/Else statement that gives a discount if more footage of cable is bought
    Cost = calcCost(FOC_installed, 0.7)
else:
    Cost = calcCost(FOC_installed, 0.87)

print("Thank you for shopping with the Fiber Optic Calculator.")
print("The total fiber installation cost for", Cname, "is", '$%.2f'%Cost)
    # Receipt with cost of installation
