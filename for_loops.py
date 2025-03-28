# Task 1
def task_1():
    word = input("Type a word: ")
    for i in range(25):
        print(word)

# Task 2
def task_2():
    word = input("Type a word: ")
    for i in range(200):
        print(word + ' ', end='')

# Task 3
def task_3():
    for i in range(5, 91):
        print(i, ' ', end='')

# Task 4
def task_4():
    for i in range(2, 103, 4):
        print(i)

# Task 5
def task_5():
    number = 29
    for i in range(number):
        print(number)
        number -= 1
        if(number == 4):
            break

    for i in range(29, 4, -1):
        print(i)

# Task 6
def task_6():
    for i in range(1, 6):
        print(i, '.', "A")

# Task 7
def task_7():
    for i in range(20):
        print(i**2, ' ', end='')

# Task 8
def task_8():
    for i in range(40):
        print("A", end='')
    for i in range(50):
        print("B", end='')

# Task 9
def task_9():
    for i in range(100):
        print("ACB", end='')

# Task 10
def task_10():
    for i in range(10):
        print("A", end='')
    for i in range(5):
        print("BCD", end='')
    print("E", end='')
    for i in range(15):
        print("F", end='')

# Task 11
def task_11():
    number = int(input("Enter a number: "))
    for i in range(number):
        print("Word ", end='')

# Task 12
def task_12():
    for i in range(10):
        number = int(input("Enter a number and I'll give you the square: "))
        print("Square is", number * 2)

# Task 13
def task_13():
    height = int(input("Enter height: "))
    for i in range(height):
        print(10 * "*")

# Task 14
def task_14():
    size = eval(input("Enter size: "))
    for i in range(size - 1):
        print("*", end='')
    for i in range(size - 2):
        print("*")
    for i in range(size):
        print("*", end='')

