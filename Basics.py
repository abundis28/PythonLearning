import math

# Demonstration of how operators are used in Python
def arithmetics(x, y):
    print("Sum: ", x + y)
    print("Floating point sum: ", float(x) + float(y))
    print("Substraction: ", x - y)
    print("Exponential (first^second): ", x ** y)
    print("Negative Exponential: ", x ** -y)
    print("Division: ", x / y)
    print("Division: ", math.ceil(x / y))
    print("Rounded-up division: ", math.ceil(x / y))
    print("Integer Division: ", x // y)
    print("Mod: ", x % y)

def showMenuOptions():
    print("--- Please select a demonstration option to run: ")
    print("1. Operators (integers and floating point)")
    print("4. Exit program")
    option = int(input())
    return option

### MAIN ###
print("Welcome to the Python basics demonstration!!!")
print()
option = showMenuOptions()
print()
while option != 4:
    if option == 1:
        x = int(input("Type first number for the demonstration: "))
        y = int(input("Type second number for the demonstration: "))
        print(arithmetics(x, y))
    elif option == 2:
        print("Run second option")
    elif option == 3:
        print("Run third option")
    print()
    option = showMenuOptions()

print("Thanks for running this code!")
