# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have. 
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.
import math

def askMoneyApple():
    global money
    global appleprice
    money = int(input("Enter the amount of money you have: ₱ "))
    appleprice = int(input("Enter apple price: ₱ "))
    return money, appleprice

def operation2(moneyF, appleF):
    global apple_total
    apple_total = moneyF/appleF
    return math.floor(apple_total)

def operation(moneyF, appleF):
    apple_total = int(moneyF/appleF)
    cost_total = appleF*apple_total
    money_change = moneyF - cost_total
    return money_change

def display(apple, change): 
    if apple < 2: print(f"You can buy {apple} apple and your change is ₱{change: .2f}.")
    else: print(f"You can buy {apple} apples and your change is ₱{change: .2f}.")

# 1. ask money, ask apple price
ask_money_and_apple = askMoneyApple()

# 2.  maximum apples and change
apple_total = operation2(money, appleprice)
appleQuant_change = float(operation(money, appleprice))

# 3. display apple total, display change
display(apple_total, appleQuant_change)