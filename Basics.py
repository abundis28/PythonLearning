# Demonstration of how operators are used in Python
def operators(x, y):
    print("Sum: ", x + y)
    print("Substraction: ", x - y)
    print("Exponential (first^second): ", x ** y)
    print("Division: ", x / y)
    print("Integer Division: ", x // y)
    print("Mod: ", x % y)

### MAIN ###
print("Welcome to the Python basics demonstration!!!")
print()
option = int(input("Please select an option of demonstration to run: "))
print()
while option != 4:
    if option == 1:
        x = int(input("Type first number for the operators demonstration: "))
        y = int(input("Type second number for the operators demonstration: "))
        print(operators(x, y))
    elif option == 2:
        print("Run second option")
    elif option == 3:
        print("Run third option")
    print()
    option = int(input("Please select another option of demonstration to run: "))

print("Thanks for running this code!")
