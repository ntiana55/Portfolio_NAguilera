# DSC 510
# 10.1 Programming Assignment
# Cash Register Program
# Nicole Aguilera
# 08/10/2020

import locale

locale.setlocale(locale.LC_ALL, 'en_CA.UTF-8')

print("Welcome to the Cash Register.\n")

class CashRegister():

    itemCount = 0
    totalPrice = 0.0

    def __init__(self):
        pass

    def addItem(self, price):
        self.itemCount = self.itemCount + 1
        self.totalPrice = self.totalPrice + price

    def getTotal(self):
        return self.totalPrice

    def getCount(self):
        return self.itemCount

cart = CashRegister()

looping = True
while looping == True:
    answer = input('Would you like to enter an item?')
    if answer == "Y" or answer == "y" or answer == "Yes" or answer == "yes":
        price = float(input("Please enter the price of your item:"))
        cart.addItem(price)
    elif answer == "N" or answer == "n" or answer == "No" or answer == "no":
        break
    else:
        print("That was not a valid response. Please enter yes or no.")

cart.totalPrice = locale.currency(cart.totalPrice)

print("\nYou have", cart.getCount(), "in your cart. Your total is", cart.getTotal())
print("Thank you for shopping with the Cash Register.")



