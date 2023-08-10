# variables
symbol = ["+", "-", "*", "/"]

# functions


def FuckYou():
    print("\nNuh uh\n")
    exit()


def Checker(x):
    if x.isnumeric() == True:
        global y
        y = int(x)
    else:
        FuckYou()


# number1
number1 = input("chose first number:\n")
Checker(number1)
n1 = y

# number2
number2 = input("chose second number:\n")
Checker(number2)
n2 = y

# number3
number3 = input("chose symbol:\n")

if number3 not in symbol:
    FuckYou()


if number3 == "+":
    print("\n Addition")
    print("\n", n1 + n2, "\n")

if number3 == "-":
    print("\n Substraction")
    print("\n", n1 - n2, "\n")

if number3 == "*":
    print("\n Multiplication")
    print("\n", n1 * n2, "\n")

if number3 == "/":
    if n2 == 0:
        FuckYou()
    print("\n Division")
    print("\n", n1 / n2, "\n")
