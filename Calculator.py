def welcome():
    print("Welcome to Python Calculator!\nPlease following the instruction below:  ")
    print("\nPlease select a number to calculate")
    print("1 for Add")
    print("2 for Subtraction")
    print("3 for Multiplication")
    print("4 for Division")


def add(x, y):
    return float(x) + float(y)


def subtract(x, y):
    return float(x) - float(y)


def multiply(x, y):
    return float(x) * float(y)


def divide(x, y):
    return float(x) / float(y)


def again():
    message = input("Please enter 'y' continue calculate otherwise enter 'n' Exit this program: ")

    if message.upper() == 'Y':
        calculator()
    elif message.upper() =='N':
        print("Thanks!")
    else:
        again()


def calculator():
    x = input("Please enter your first number: ")
    choice = input("Please enter your arithmetic code\n(Example: 1 + 2, enter '2' to calculate Add arithmetic): ")
    y = input("Please enter you second number: ")

    if choice == "1":
        print(x, "+", y, "=", add(x, y))
    elif choice == "2":
        print(x, "-", y, "=", subtract(x, y))
    elif choice == "3":
        print(x, "*", y, "=", multiply(x, y))
    elif choice == "4":
        print(x, "/", y, "=", divide(x, y))
    else:
        print("Wrong enter, please only select one of four arithmetic")
    again()


welcome()
calculator()
