# Task 1
def task_1():
    word = input("Enter a programming language: ")
    if (word == "python"):
        print("This program was written in python")


# Task 2
def task_2():
    number = int(input("Enter a number: "))
    if (number < 0):
        print("Number can't be negative ")
    else:
        print(f"The Square root of {number} is {int(number ** (1 / 2))}")


# Task 3
def task_3():
    while True:
        temperature = int(input("Enter temperature in Celsius: "))
        if (temperature <= 0):
            print("Warning, low temperature!")
        elif (temperature > 0 and temperature < 35):
            print("Temperature is normal")
        else:
            print("Warning, high temperature")


# Task 4
def task_4():
    days = int(input("Enter number of days: "))
    if (days == 29 or days == 28):
        print("February")
    elif (days == 30):
        print("April, June, September, November")
    elif (days == 31):
        print("January, March, May, July, August, October, December")
    else:
        print("Error")


# Task 5
def task_5():
    while True:
        length_feet = float(input("Enter the length in feet: "))
        convert_to = input("Which unit do you want to convert to: ")
        in_lower = convert_to.lower()

        if (in_lower == "meters"):
            converted = length_feet * 0.3048
            print(f"That is {converted} meters")
        elif (in_lower == "inches"):
            converted = length_feet * 12
            print(f"That is {converted} inches")
        elif (in_lower == "centimeters"):
            converted = length_feet * 30.48
            print(f"That is {converted} centimeters")
        else:
            print("Error")


# Task 6
def task_6():
    number = int(input("Enter a number in the range of 20 to 99: "))
    if (19 < number < 30):
        print("Twenty")
    elif (29 < number < 40):
        print("Thirty")
    elif (39 < number < 50):
        print("Forty")
    elif (49 < number < 60):
        print("Fifty")
    elif (59 < number < 70):
        print("Sixty")
    elif (69 < number < 80):
        print("Seventy")
    elif (79 < number < 90):
        print("Eighty")
    elif (89 < number < 100):
        print("Ninety")
    else:
        print("Invalid input")


# Task 7
def task_7():
    number = int(input("Enter a number: "))
    if (number == 0 or number == 2 or 9 < number < 16 or 19 < number < 26):
        print("Okay")


# Task 8
def task_8():
    number = eval(input("Enter a number: "))
    if (number % 7 == 0):
        print("Divisible by 7")


# Task 9
def task_9():
    for i in range(0, 101):
        if (i % 3 == 0 or i % 7 == 0) and not (i % 3 == 0 and i % 7 == 0):
            print(i)


# Task 10
def task_10():
    import random as r
    for i in range(100):
        number = r.randint(0, 1)
        if (number == 0):
            print(f"{number}? ", end='')
        else:
            print(f"{number}* ", end='')


# Task 11
def task_11():
    import random as r
    lista = ["A", "B", "C", "D", "E"]
    random_element = r.choice(lista)
    print(random_element)

    # Using if statements instead of random.choice
    number = r.randint(0, 4)
    if (number == 0):
        print("A")
    elif (number == 1):
        print("B")
    elif (number == 2):
        print("C")
    elif (number == 3):
        print("D")
    elif (number == 4):
        print("E")


# Task 12
def task_12():
    import random
    for i in range(100):
        numer = random.randint(0, 2)
        if (numer == 1 or numer == 2):
            print("1", end='')
        else:
            print("0", end='')


# Task 13
def task_13():
    hour = int(input("What time do you start: "))
    hour2 = int(input("What time do you leave: "))
    rate = 5.50
    if (hour2 > hour):
        print(f"You will pay {(hour2 - hour) * rate}")
    elif (hour > hour2):
        print(f"You will pay {((hour2 - hour) % 24) * rate}")


# Task 14
def task_14():
    for i in range(0, 201):
        if not (i % 10 == 8):
            print(f"file{i}.jpg")


# Task 15
def task_15():
    number = int(input("Enter a number: "))
    for i in range(30):
        if (number == 1):
            break
        elif (number % 2 == 0):
            number = number // 2
            print(number)
        elif (number % 2 != 0):
            number = 3 * number + 1
            print(number)


# Task 16
def task_16():
    for x in range(0, 10000000):
        xd = 21 * x ** 2 - x ** 3 + 21904
        if (xd == 0):
            print(f"The result is {x}")


# Task 17
def task_17():
    import random as r
    for i in range(10):
        number1 = r.randint(20, 51)
        number2 = r.randint(20, 51)
        number3 = r.randint(20, 51)
        equation = number1 + number2 + number3
        answer = int(input(f"{number1} + {number2} + {number3} = "))

        if (answer == equation):
            print("Good!")
        elif (-5 <= answer - equation):
            print("Close")
        else:
            print("Wrong")
