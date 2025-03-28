# Task 1
def task_1():
    text = 'Didn\'t Hamlet say "To be or not to be"? '
    print(text)

# Task 2
def task_2():
    string = """A
    B
    \\
    C\tD """
    print(string)

# Task 3
def task_3():
    string = input("Enter a string of at least 6 characters: ")
    print(f"Length of that string is {len(string)}")
    print(f"2nd char of that string is {string[1]}")
    print(f"Last char of that string is {string[-1]}")
    print(f"First 5 chars of that string are {string[:5]}")
    print(f"Last 2 chars of that string are {string[-2:]}")
    print(f"String backwards is {string[::-1]}")
    print(f"All chars except last one {string[:-1]}")
    print(f"All chars except first and last {string[1:-1]}")
    if string.find('a') != 0:
        print(f"First occurrence of 'a' {string.find('a')}")
    else:
        print("No letter 'a'")
    print(string.upper())
    print(string.replace(' ', '_'))

# Task 4
def task_4():
    string1 = input("Enter string 1: ")
    string2 = input("Enter string 2: ")
    print(10 * string1)
    print(string1 + string2)

# Task 5
def task_5():
    string = input("Enter a number: ")
    if string.find('.') != 0:
        print("It's a floating point number")
    else:
        print("It's an integer")

# Task 6
def task_6():
    language = input("Enter a programming language: ")
    language_lower = language.lower()
    if language_lower == "python":
        print("You are using python")

# Task 7
def task_7():
    string = input("Enter text: ")
    if '.' in string or ',' in string or ':' in string:
        print("There is some punctuation")
    else:
        print("No punctuation found")

# Task 8
def task_8():
    sentence = input("Enter a sentence: ")
    no_spaces = sentence.replace(' ', '')
    upper = no_spaces.upper()
    print(upper)

# Task 9
def task_9():
    string = input("Enter a string: ")
    string = string.replace(' ', '*')
    t = ''
    for i in range(len(string)):
        if i % 5 == 0:
            t += '!'
        else:
            t += string[i]
    t = t * 3
    print(t)

# Task 10
def task_10():
    string = input("Enter a string: ")
    if len(string) >= 5:
        new_string = string + "***"
    else:
        number = 5 - len(string)
        new_string = string + number * '!'
    print(new_string)

# Task 11
def task_11():
    string = input("Enter text here: ")
    for i in range(len(string)):
        print(string[i], ' ', end='')

# Task 13
def task_13():
    string = input("Enter a sentence: ")
    string = string.upper()
    As = []
    Bs = []
    for i in range(len(string)):
        if string[i] == 'A':
            As.append(string[i])
        elif string[i] == 'B':
            Bs.append(string[i])
    if len(As) > len(Bs):
        print("More As than Bs")
    elif len(As) < len(Bs):
        print("More Bs than As")
    else:
        print("Same amount of As and Bs")

# Task 14
def task_14():
    string = input("Enter a sentence: ")
    letters_count = 0
    for i in range(len(string)):
        if string[i].isalpha():
            letters_count += 1
    print(f"This sentence has {letters_count} letters")

# Task 15
def task_15():
    string = input("Enter a string: ")
    lower_count = 0
    upper_count = 0
    for i in range(len(string)):
        if string[i].islower():
            lower_count += 1
        elif string[i].isupper():
            upper_count += 1
    if lower_count > upper_count:
        print("More lowercase letters than uppercase")
    elif lower_count < upper_count:
        print("More uppercase letters")
    else:
        print("Same amount of uppercase and lowercase letters")

# Task 16
def task_16():
    string = input("Enter a sentence here: ")
    for i in 'abcdefghijklmnopqrstuvwxyz':
        if i not in string:
            print(i, end='')

# Task 17
def task_17():
    string1 = input("Enter a string here: ")
    string2 = input("Enter a string here: ")
    xd = False
    for i in string1:
        if i.isalpha():
            if not i in string2:
                xd = True
    if xd:
        print("String 1 contains letters that are not in string 2")
    else:
        print("No letters in string 1 that are not in string 2")

# Task 18
def task_18():
    string1 = input("Enter string1 here: ")
    string2 = input("Enter string2 here: ")
    difference_counter = 0
    if len(string1) != len(string2):
        print("Strings have different lengths")
    else:
        for i in range(len(string2)):
            if string1[i] != string2[i]:
                difference_counter += 1
                index = i
    if difference_counter == 1:
        print(f"String1 and string2 are different in exactly 1 position and that is index {index}")

# Task 19
def task_19():
    import random as r
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for i in range(10):
        letter = alphabet[r.randint(0, len(alphabet) - 1)]
        print(letter, end='')

# Task 21
def task_21():
    string1 = input("Enter a string in lowercase: ")
    if string1.islower():
        for i in 'abcdefghijklmnopqrstuvwxyz':
            if i in string1:
                print(f"Letter {i} is in string 1 on index {string1.find(i)}")
            else:
                print(f"Letter {i} not in string 1")
    else:
        print("String must be lowercase")

# Task 20
def task_20():
    import random as r
    print('This program generates a random word using the letters from a word provided by a user')
    string1 = input("Enter a string: ")
    string1 = string1.replace(' ', '')
    for i in range(10):
        index = r.randint(0, len(string1) - 1)
        print(string1[index], end='')

