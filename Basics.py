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

# Demonstration of conditions in Python
def conditions(i, j):
    print("Numbers are different from 0: ", bool(i) and bool(j))
    if i > 0 and j > 0:
        print("Both numbers are positive.")
    elif i > 0:
        print("First number is positive, second is negative.")
    else:
        print("First number is negative, second is positive.")

# Demonstration of cycles in Python
def cycleString(word):
    for char in word:
        print(char)

def cycleNum(n, m):
    print("From first number to second number to the 3rd power: ")
    for i in range(n, m):
        print(i ** 3)
    print("2^i, from 0 to second number:")
    for i in range(m):
        print(2 ** -i)
    print("From 0 to -20 with step equal to second number: ")
    for i in range(0, -20, -n):
        print(i)

def showMenuOptions():
    print("--- Please select a demonstration option to run: ")
    print("1. Math Operators (integers and floating point)")
    print("2. Conditions")
    print("3. Cycles")
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
        i = int(input("Type first number for the demonstration: "))
        j = int(input("Type second number for the demonstration: "))
        print(conditions(i, j))
    elif option == 3:
        word = str(input("Type word for iteration demonstration: "))
        print(cycleString(word))
        n = int(input("Type first number for the demonstration: "))
        m = int(input("Type second number for the demonstration: "))
        print(cycleNum(n, m))
    print()
    option = showMenuOptions()

print("Thanks for running this code!")
