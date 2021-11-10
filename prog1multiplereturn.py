def getnameageaddress():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    return name, age, address

def display(nameF, ageF, addressF):
    print(f"Hi I am {nameF}. I am {ageF} years old, from {addressF}. ")

# ask name age address

name, age, address = getnameageaddress()

# display
display(name, age, address)