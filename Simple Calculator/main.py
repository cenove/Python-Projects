import subprocess

x = 0
y = 0

def Sum(x, y):
    print(x + y)

def Subtract(x, y):
    print(x - y)

def Multiply(x, y):
    print(x * y)

def Division(x, y):
    print(x / y)

while True:

    print("SIMPLE CALCULATOR\n")
    print(" 1 - Sum\n",
        "2 - Subtract\n",
        "3 - Multiply\n",
        "4 - Division\n",
        "5 - About\n",
        "6 - Quit\n")

    option = int(input())

    match option:
        case 1:
            print("\nInput the value of x: ")
            x = int(input())
            print("\nInput the value of y:")
            y = int(input())
            Sum(x, y)
            option = 9

        case 2:
            print("\nInput the value of x: ")
            x = int(input())
            print("\nInput the value of y:")
            y = int(input())
            Subtract(x, y)
            option = 9

        case 3:
            print("\nInput the value of x: ")
            x = int(input())
            print("\nInput the value of y:")
            y = int(input())
            Multiply(x, y)
            option = 9

        case 4:
            print("\nInput the value of x: ")
            x = int(input())
            print("\nInput the value of y:")
            y = int(input())
            Division(x, y)
            option = 9

        case 5:
            print("---------------------------------------------------------------------------------------------")
            print("For now it's only a simple calculator, but I have the following plans to make it better:",
                "\n- Add more values instead of only two",
                "\n- Add an interface with Tkinter",
                "\n- Add more ways to calculate (porcentage, sqr, sen, cos, tg and etc.)")
            print("---------------------------------------------------------------------------------------------")

        case 6:
            quit

        case 9:
            print("SIMPLE CALCULATOR\n")
            print(" 1 - Sum\n",
                "2 - Subtract\n",
                "3 - Multiply\n",
                "4 - Division\n",
                "5 - About\n",
                "6 - Quit")

        case _:
            subprocess.run("cls")
            print("There's no option for that\n")
            option = 9
            
            
