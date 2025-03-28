import random
from itertools import permutations

def task1():
    users_input = input("Enter a list of at least 4 numbers separated by spaces: ")
    users_list = users_input.split()
    random_choice = random.choice(users_list)
    random_three = random.sample(users_list, 3)
    random.shuffle(users_list)
    print(f"Random choice: {random_choice}")
    print(f"Random three: {random_three}")
    print(users_list)

def task2():
    coin_flips = [random.choice("HT") for _ in range(100)]
    print(random.choice(coin_flips))
    print("".join(coin_flips))

def task3():
    char_list = 60 * ['A'] + 30 * ['B'] + 8 * ['C'] + 2 * ['D']
    print("".join(random.choices(char_list, k=1000)))

def task4():
    password_length = int(input("Enter your password's length: "))
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()'
    password = "".join(random.choice(chars) for _ in range(password_length))
    print(f'Your random password is {password}, don\'t forget it!')

def task5():
    verbs = ['goes', 'does', 'is', 'makes', 'talks', 'screams', 'walks', 'swims', 'reads', 'sings']
    adjectives = ['beautiful', 'big', 'small', 'old', 'new', 'dirty', 'ugly']
    nouns = ['dog', 'cat', 'person', 'car', 'truck', 'building', 'bottle']
    sentence = f"The {random.choice(adjectives)} {random.choice(nouns)} {random.choice(verbs)} the {random.choice(nouns)}."
    print(sentence)

def task6():
    verbs = ['goes', 'does', 'is', 'makes', 'talks', 'screams', 'walks', 'swims', 'reads', 'sings']
    adjectives = ['beautiful', 'big', 'small', 'old', 'new', 'dirty', 'ugly']
    nouns = ['dog', 'cat', 'person', 'car', 'truck', 'building', 'bottle']
    adjective = random.choice(adjectives)
    noun1 = random.choice(nouns)
    nouns.remove(noun1)
    verb = random.choice(verbs)
    noun2 = random.choice(nouns)
    sentence = f"The {adjective} {noun1} {verb} the {noun2}."
    print(sentence)

def task7():
    card_suits = ['Diamonds', 'Hearts', 'Spades', 'Clubs']
    card_ranks = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace']
    deck = [f"{rank} of {suit}" for suit in card_suits for rank in card_ranks]
    random.shuffle(deck)
    print(f"Your cards are {deck[:5]}")

def task8():
    users_input = input("Enter a word: ")
    replace_indices = random.sample(range(len(users_input)), min(3, len(users_input)))
    masked_word = ''.join('*' if i in replace_indices else users_input[i] for i in range(len(users_input)))
    print(masked_word)

def task9():
    users_string = input("Enter a word: ")
    indices = list(range(len(users_string)))
    users_string_list = list(users_string)
    for _ in range(len(users_string)):
        random_index = random.choice(indices)
        users_string_list[random_index] = '*'
        indices.remove(random_index)
        print(''.join(users_string_list))

def task10():
    numbers = list(range(1, 21))
    for _ in range(3):
        a, b = random.sample(range(len(numbers)), 2)
        numbers[a], numbers[b] = numbers[b], numbers[a]
    print(numbers)

def task11():
    sentence = input("Enter some words separated by spaces: ")
    print(' '.join(sentence.split()))

def task12():
    emails = input("Enter all the email addresses: ")
    print(';'.join(emails.split()))

def task13():
    date = input("Enter a date in the following format: day/month/year: ")
    for part in date.split('/'):
        print(part)

def task14():
    users_input = input("Enter some words separated by spaces: ")
    print(' '.join(word.capitalize() for word in users_input.split()))

def task15():
    for perm in permutations('abcd'):
        print(''.join(perm))

def task16():
    users_input = input("Enter a couple of sentences here: ")
    for sentence in users_input.split('.'):
        words = sentence.strip().split()
        if words:
            print(words[-1])

def task17():
    print([round(x**0.5, 2) for x in range(1, 101)])

def task18():
    users_input = input("Enter some numbers: ").split()
    categorized = [[x for x in users_input if 90 <= int(x)],
                   [x for x in users_input if 80 <= int(x) < 90],
                   [x for x in users_input if 70 <= int(x) < 80],
                   [x for x in users_input if 60 <= int(x) < 70],
                   [x for x in users_input if 50 <= int(x) < 60]]
    print(categorized)

def task19():
    matrix = [[random.randint(0, 9) for _ in range(6)] for _ in range(6)]
    for row in matrix:
        print(row)
    zero_count = sum(row.count(0) for row in matrix)
    print(f'Total zeros: {zero_count}')

def task20():
    battleships = [[random.randint(0, 1) for _ in range(10)] for _ in range(10)]
    row, col = map(int, input("Enter coordinates: ").split())
    print("HIT!" if battleships[row][col] == 1 else "MISS!")

def task21():
    matrix = [[random.randint(0, 2) for _ in range(6)] for _ in range(6)]
    for row in matrix:
        print(row)
    start_row, end_row, start_col, end_col = map(int, input("Enter row and column range: ").split())
    total = sum(matrix[i][j] for i in range(start_row, end_row + 1) for j in range(start_col, end_col + 1))
    print(f'Sum of selected range: {total}')

