# Task 1
def task_1():
    x = int(input("Enter x: "))
    y = int(input("Enter y: "))
    print(x ** y)


# Task 2
def task_2():
    a = int((9 + 3) / (8 - 2))
    print(a)


# Task 3
def task_3():
    import math
    cards = int(input("How many cards do you have? "))
    reduced = cards // 2
    print(reduced)


# Task 4
def task_4():
    a = float(input("Enter number a: "))
    b = float(input("Enter number b: "))
    modulus = abs(a - b)
    print(modulus)


# Task 5
def task_5():
    number = int(input("Enter a positive number: "))
    sq_root = number ** (1 / 2)
    rounded = round(sq_root, 2)
    print(rounded)


# Task 6
def task_6():
    for i in range(20):
        print(i, " and the square root of this is: ", round(i ** (1 / 2), 4))


# Task 7
def task_7():
    import math as m
    height = int(input("Enter height: "))
    width = int(input("Enter width: "))
    angle = m.atan2(height, width)
    angle_degrees = m.degrees(angle)
    print("The angle is: ", angle_degrees)


# Task 8
def task_8():
    hour = int(input("Enter the hour: "))
    scale = int(input("Enter how much you want to shift: "))
    new_hour = (hour + scale) % 24
    print(f"The new hour will be {new_hour}")


# Task 9
def task_9():
    inches_height = int(input("Enter your height in inches: "))
    feet_height = inches_height // 12
    rest = inches_height % 12
    print(f"Your height in feet is {feet_height} feet and {rest} inches")


# Task 10
def task_10():
    import random
    number1 = random.randint(1, 10)
    number2 = random.randint(1, 10)
    print(f"Random numbers are {number1} and {number2}, and their sum is {number1 + number2}")


# Task 11
def task_11():
    import random
    for i in range(100):
        number = random.randint(50, 60)
        print(number, end='   ')


# Task 12
def task_12():
    import random
    letter = input("Enter a letter: ")
    number = random.randint(1, 10)
    for i in range(number):
        print(number * letter, end='')


# Task 13
def task_13():
    import random
    number = int(input("Enter a positive integer: "))
    random_number = random.randint(number, number + 10)
    for i in range(random_number):
        print("A", end='')


# Task 14
def task_14():
    import random
    xd = 10
    for i in range(50):
        for i in range(xd):
            number = random.randint(0, 1)
            print(number, end='')
        print()
        xd += 1


# Task 15
def task_15():
    print("You will be asked to enter the year, month, and day in this order.")
    year = int(input("Enter the year: "))
    month = int(input("Enter the month: "))
    day = int(input("Enter the day: "))

    p = (14 - month) // 12
    q = year - p
    r = q + q // 4 - q // 100 + q // 400
    s = month + 12 * p - 2
    t = (day + r + (31 * s) // 12) % 7

    if t == 0:
        print("Sunday")
    elif t == 1:
        print("Monday")
    elif t == 2:
        print("Tuesday")
    elif t == 3:
        print("Wednesday")
    elif t == 4:
        print("Thursday")
    elif t == 5:
        print("Friday")
    elif t == 6:
        print("Saturday")
