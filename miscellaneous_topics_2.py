import math
import random
from calendar import month
from random import choice, shuffle
from string import digits


def task_1():
    course_code = input("Enter a course code: ")
    # space_index = course_code.find(' ')
    # digits = int(course_code[space_index+1:])
    digits = int(course_code.split()[1])
    print(digits)

    if 499 < digits or digits < 100:
        print("Invalid Code")
    else:
        print("Thank you!")


def task_2():
    users_input = input("Enter several numbers separeted by semicolons: ")
    lista = users_input.split(';')
    list_of_numbers = [int(x) for x in lista]
    sum_of_numbers = sum(list_of_numbers)
    print(sum_of_numbers)


def task_3():
    number = input("Enter a number with a coma in it: ")
    sqr_root = math.sqrt(float(number.replace(',', '')))
    print(sqr_root)

def task_4():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    lista = [letter+str(number) for letter, number in zip(alphabet,  range(1, 27))]
    print(lista)

def task_5():
    sentence = input("Enter a sentence that contains a positive integer: ")

    updated_sentence = ''.join([str(int(char) + 1) if char.isdigit() else char for char in sentence])
    print(updated_sentence)

def task_6():
    for i in range(100, 121):
        lista = list(str(i))
        random.shuffle(lista)
        new_i = ''.join(lista)
        print(i, new_i)

def task_7():
    length = int(input("Enter the length of your password: "))
    possible_letters = 'abcdefghijklmnopqrstuvwzyz'
    possible_letters_upper = possible_letters.upper()
    possible_characters = '!@#$%^&*().'
    possible_digits = '1234567890'
    all_chars = possible_letters + possible_letters_upper + possible_characters + possible_digits

    password = (choice(possible_characters) + choice(possible_letters)
                + choice(possible_letters_upper) + choice(possible_digits))


    for i in range(length - 4):
        password += choice(all_chars)

    lista = list(password)
    shuffle(lista)
    generated_password = ''.join(lista)

    print(generated_password)


def task_8():

    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
              'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    for i in range(10):
        r = random.randint(0, 11)
        print(months[r], random.randint(1, days[r]))


def task_9():

    multiplication_tasks = []
    answers = []
    points = 0

    for i in range(10):
        number_1 = random.randint(1, 12)
        number_2 = random.randint(1, 12)

        task = f'{number_1} x {number_2}'
        answer = number_2*number_1
        multiplication_tasks.append(task)
        answers.append(answer)

    for i in range(10):
        users_answer = int(input(f"What's {multiplication_tasks[i]}? "))
        if users_answer == answers[i]:
            print("Correct!")
            points += 1
        else:
            print("Wrong!")
    print(f"You scored {points} points")

def task_10():

    multiplication_tasks = []

    for i in range(20):
        x = random.randint(2, 12)
        while x == 10:
            x = random.randint(2, 12)
        y = random.randint(2, 12)
        while y == 10:
            y = random.randint(2, 12)

        multiplication_tasks.append(f'{x} x {y}')

    print(multiplication_tasks)

    # (b) Using choice
    # from random import choice
    #
    # numbers = [2, 3, 4, 5, 6, 7, 8, 9, 11, 12]
    # tasks = [str(choice(numbers)) + ' x ' + str(choice(numbers)) for i in range(20)]
    # print(tasks)

def task_11():
    days_in_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    while True:
        date = input("Enter a date in the month/date format: ")
        splited = date.split('/')
        day = int(splited[1])
        month = int(splited[0])

        if day > days_in_months[month-1] or month > 12:
            print("Not a real date ")
        else:
            print("Real date")

def task_12():
    angle = input("Enter an angle in degrees-minutes-seconds form, such as 49d33'22'' or 153d4'22'': ")


    degrees = int(angle.split('d')[0])
    minutes = int(angle.split('d')[1].split("'")[0])
    seconds = int(angle.split("'")[1])

    decimal_angle = degrees + minutes/60 + seconds/3600

    print(f"{angle} converted to decimal is {round(decimal_angle, 2)}")

def task_13():
    prizes = eval(input("Enter a list of prizes: "))

    for x in prizes:
        print('{:5}'.format(x * 1.06))

def task_14():
    for i in range(0, 390, 30):
        sinus = math.sin(math.radians(i))
        cosinus = math.cos(math.radians(i))

        print('{:3}    {:6.3f}    {:6.3f}'.format(i, sinus, cosinus))


def task_15():
    Names = ['Alice', 'Bob', 'Caroline']
    Birthdays = ['2/7/86', '11/12/66', '8/17/72']
    Salaries = [72000, 144300, 43200]

    for i in range(len(Names)):
        day, month, year = Birthdays[i].split('/')
        day = int(day)
        month = int(month)

        print('{:12}    {:02d}/{:02d}/{:2s}    {:,d}'.format(Names[i], day, month, year, Salaries[i]))

def task_16():
    for i in range(1, 10):
        for j in range(1, 10):
            print(f'({i}, {j})', end='')
        print()


def task_17():
    for i in range(1, 10):
        for j in range(1, 10):
            if i > j:
                print(f'({i}, {j})', end='')
        print()

def task_18():
    for x in range(-100, 101):
        for y in range(-100, 101):
            if (37 * x + 14 *y == 11):
                print(f'x={x}, y={y}')

def task_19():
    integers = eval(input("Enter a list of integers: "))
    i = 1

    while i < len(integers) and integers[i] != integers[i-1]:
        i += 1
    if i < len(integers):
        print(i)
    else:
        print('no repeats')

def task_20():
    lista = [[random.randint(1, 3) for _ in range(6)] for _ in range(6)]

    for row in lista:
        print(row)

    location = input("Enter coordinates in x,y format: ")
    row = int(location.split(',')[0])
    column = int(location.split(',')[1])


    sum_of_neighbours = 0

    for dx in [-1, 0, 1]:
        for dy in[-1, 0, 1]:
            if dx == 0 and dy == 0:
                continue
            new_row = row + dx
            new_column = column + dy

            if 0 <= new_row < len(lista) and 0 <= new_column < len(lista[0]):
                sum_of_neighbours += lista[new_row][new_column]


    print(f'Sum of all neighbours of number at row {row}, column {column} is {sum_of_neighbours}')








