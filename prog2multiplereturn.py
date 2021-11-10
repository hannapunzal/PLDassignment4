# Create a program that will ask how many apples and oranges you want to buy. 
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format. The total amount is ______.

def applesNorangesQuant():
    global appleQuant
    global orangeQuant
    appleQuant = int(input("How many apples do you want to buy? "))
    orangeQuant = int(input("How many oranges do you want to buy? "))
    return appleQuant, orangeQuant

def totalamount(sum):
    appletotal = 20*appleQuant
    orangetotal = 25*orangeQuant
    sum = float(appletotal + orangetotal)
    return sum

def display(totalF):
    print(f"Hi, the total amount for apples and oranges is ₱{totalF: .2f}. Thank you!")

appleprice = 20
orangeprice = 25

# 1. ask how many apples and oranges you want to buy
apple_orange_Quant = applesNorangesQuant()

# 2. display total amount 
total = totalamount(apple_orange_Quant)
# 3. display output
display(total)

