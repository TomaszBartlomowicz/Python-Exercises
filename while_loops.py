import random
import os


def task_1():
    i = 2
    print(i, end=' ')
    while i < 20:
        i += 3
        print(i, end=' ')
    print()


def task_2():
    i = 100
    print(i, end=' ')
    while i > 1:
        i -= 1
        print(i, end=' ')
    print()


def task_3():
    user_number = 0
    total = 0
    while user_number >= 0:
        user_number = int(input("Enter a number: "))
        if user_number >= 0:
            total += user_number
    print(total)


def task_4():
    numbers_count = 0
    user_number = -1
    flag = False
    while user_number != 5:
        user_number = int(input("Enter a number from 1 to 10: "))
        if 1 <= user_number <= 10:
            numbers_count += 1
        if user_number == 3:
            flag = True
    print(numbers_count)
    if flag:
        print("yes")


def task_5():
    user_input = ""
    while len(user_input) < 5:
        user_input = input("Enter a string of at least 5 characters: ")
    print(user_input)


def task_6():
    user_input = ""
    while len(user_input) < 5:
        user_input = input("Enter a string of at least 5 characters: ")
    print(user_input)
    index = -1
    while index < 0 or index >= len(user_input):
        index = int(input("Enter a valid index: "))
    print(user_input[index])


def task_7():
    while True:
        s = input("Enter a string: ")
        if s == "":
            break
        print("It's a palindrome!" if s == s[::-1] else "Not a palindrome.")


def task_8():
    user_number = int(input("Enter a number from 20 to 100: "))
    while user_number > 0:
        user_number -= random.randint(1, 10)
        print(user_number)


def task_9():
    number = int(input("Enter a starting value: "))
    while number != 1:
        number = number // 2 if number % 2 == 0 else (3 * number) + 1
        print(number)


def task_10():
    numbers = []
    tens_count = 0
    while tens_count <= 5:
        number = random.randint(1, 10)
        numbers.append(number)
        if number == 10:
            tens_count += 1
    print(numbers)


def task_11():
    num_list = [random.randint(1, 5)]
    while len(num_list) < 50:
        number = random.randint(1, 5)
        if number != num_list[-1]:
            num_list.append(number)
    print(num_list)


def task_12():
    user_list = eval(input("Enter a list of numbers: "))
    for i in range(len(user_list)):
        if user_list[i] < 0:
            user_list[i] = 0
            break
    print(user_list)


def task_13():
    user_list = eval(input("Enter a list of numbers: "))
    counter = 0
    for i in range(len(user_list)):
        if user_list[i] < 0:
            user_list[i] = 0
            counter += 1
            if counter == 3:
                break
    print(user_list)


def task_14():
    user_input = input("Type something here: ")
    for char in user_input:
        if not char.isalpha():
            break
        print(char, end='xd')
    print()


def task_15():
    points = 100
    while points > 0 and points < 200:
        number = random.randint(1, 10)
        user_guess = int(input("Guess a number from 1 to 10: "))
        if user_guess < number:
            points -= 10
            print(f"Wrong! -10 points. Your points: {points}")
        elif user_guess > number:
            points -= 20
            print(f"Wrong! -20 points. Your points: {points}")
        else:
            points += 100
            print(f"Correct! +100 points. Your points: {points}")
    print("Game over!")


def task_16():
    guess_count = 3
    points = 0
    while guess_count > 0:
        number_1 = random.randint(2, 99)
        number_2 = random.randint(2, 99)
        answer = number_1 * number_2
        user_answer = int(input(f"What is {number_1} * {number_2}? "))
        if user_answer == answer:
            points += number_1 + number_2
            print(f"Correct! Your points: {points}")
        else:
            guess_count -= 1
            print(f"Wrong! You lost 1 guess. Guesses left: {guess_count}")
        if points > 50:
            print(f"You win with {points} points!")
            return
    print("You lost!")


def task_17():
    print("""
    Welcome to the game! Here's how it works:
    1. You start with $50.
    2. You will choose a number from a range (starting from 1-9).
    3. The computer will also choose a number from the same range.
    4. If your number matches the computer's number, or if your guess is outside the valid range, you owe the computer your current balance, and the game ends.
    5. If the guess is correct, your money doubles, and the range of numbers shrinks by 1 on each turn.
    6. At any time, you can type 0 to quit and keep your current winnings.
    Good luck!
    """)

    player_money = 50
    upper_range = 10

    while upper_range >= 2:
        user_guess = int(input(f"Enter a number between 1 and {upper_range}: "))
        computer_value = random.randint(1, upper_range)

        if user_guess == 0:
            print(f"You walk away with {player_money}$")
            return
        elif user_guess != computer_value and user_guess <= upper_range:
            player_money *= 2
            upper_range -= 1
            print(f"Well done, your balance now is {player_money}$")
        else:
            print(f"You lost! You owe all your money ({player_money}$) to the computer")
            return
    print(f"Congratulations! You won {player_money}$.")


def task_18():
    user_string = input("Enter a string here: ")

    while not user_string.isalpha():
        indices = [i for i in range(len(user_string)) if not user_string[i].isalpha()]
        if len(indices) == 0:
            break
        index = random.choice(indices)
        user_string = user_string[:index] + user_string[index + 1:]
        print(user_string)


def task_19():
    users_integer = int(input("Enter an integer: "))
    i = 2
    prime_numbers = []
    while users_integer > 0:
        for n in range(2, int(i**0.5 + 1)):
            if i % n == 0:
                break
        else:
            prime_numbers.append(i)
            users_integer -= 1
        i += 1
    print(prime_numbers)


def task_20():
    usres_number = int(input("Enter a positive integer: "))
    number_pool = []
    index = 1

    while True:
        random_number = random.randint(1, usres_number)
        print(f"{index}. {random_number}")
        if random_number in number_pool:
            break
        number_pool.append(random_number)
        index += 1

def task_21():
    kids = ['boy', 'girl']
    girls_count = 0
    boys_count = 0
    for i in range(10000):
        born = random.choice(kids)
        while born == 'girl':
            girls_count +=1
            born = random.choice(kids)
        boys_count += 1


    print(f"The girls are {(girls_count)/(boys_count + girls_count)*100}% of the society")


def task_22():

    longest_streak = 0

    for i in range(100000):
        random_number = random.randint(1, 10)
        current_streak = 0
        while random_number != 6:
            current_streak += 1
            random_number = random.randint(1,10)
        if current_streak > longest_streak:
            longest_streak = current_streak
    print(f"Longest streak without a 6 is {longest_streak}")

def task_23():
    my_collection = []
    packages_opened = 0

    while len(my_collection) != 100:
        packages_opened += 1
        for i in range(20):
            card = random.randint(1, 100)
            if not card in my_collection:
                my_collection.append(card)

    print(f"On avaragre you would need {packages_opened} packages opened to get a complete set")


def task_24(list1, list2):

    i, j = 0, 0
    merged = []

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged.append(list1[i])
            i += 1
        else:
            merged.append(list2[j])
            j += 1

    while i < len(list1):
        merged.append(list1[i])
        i += 1

    while j < len(list2):
        merged.append(list2[j])
        j += 1

    return merged