# Zadanie 1
def task_1():
    lista = eval(input("Enter a list: "))

    print(f"Total number of items in the list is {len(lista)}")
    print(f"4th item is {lista[3]}")
    print(f"Last 3 items are {lista[-3:]}")
    print(f"All except first 2 {lista[2:]}")
    print(f"Reversed order {lista[::-1]}")
    print(f"Sum of all items: {sum(lista)}")
    if 0 in lista:
        print(f"Zero appears at position {lista.index(0)}")
    else:
        print("no 0")
    sortedlist = sorted(lista)
    print(f"sorted list = {sortedlist}")

    del lista[0]
    print(f"List after removing the first element {lista}")

    lista[-2] = 5013
    print(f"List with second last element replaced with 5013 {lista}")

    lista.append(-500)
    print(f"List after adding 500 to the list {lista}")


# Zadanie 2
def task_2():
    a = list(100 * '0')
    print(a)


# Zadanie 3
def task_3():
    L = [1, 2, 3, 4, 5]
    copy = L

    L[0] = 999
    print(copy)
    L[0] = 1
    copy = L
    L[0] = 9
    print(copy)


# Zadanie 4
def task_4():
    L = []

    for i in range(1, 101):
        squareroot = i ** (1 / 2)
        sqr_rounded = round(squareroot, 4)
        L.append(sqr_rounded)

    print(L)


# Zadanie 5
def task_5():
    import random as r

    L = []

    for i in range(10):
        number = r.randint(1, 20)
        L.append(number)

    print(L)


# Zadanie 6
def task_6():
    import random as r

    L = []

    for i in range(20):
        number = r.randint(0, 1)
        L.append(number)

    print(L)


# Zadanie 7
def task_7():
    import random as r

    L = []
    even_count = 0

    for i in range(20):
        number = r.randint(1, 1000)
        L.append(number)

    for each_element in L:
        if each_element % 2 == 0:
            even_count += 1
    print(L)
    print(f"There are {even_count} even numbers in a list of 20 random numbers.")


# Zadanie 8
def task_8():
    L = eval(input("Enter a list of numbers from 0 to 100: "))
    L_50 = []

    for each_number in L:
        if each_number > 50:
            L_50.append(each_number)

    print(L_50)


# Zadanie 9
def task_9():
    L = eval(input("Enter a list of numbers: "))
    smallest = L[0]
    for i in range(1, len(L)):
        if L[i] < smallest:
            smallest = L[i]
            index = i
    print(f"Smallest number in the list is {smallest} at index {index}")


# Zadanie 10
def task_10():
    L = eval(input("Enter a list of numbers with some numbers greater than 10: "))

    small_more_10 = max(L)

    for i in L:
        if i > 10 and i < small_more_10:
            small_more_10 = i

    print(small_more_10)


# Zadanie 11
def task_11():
    L = eval(input("Enter a list of numbers: "))

    for i in range(len(L)):
        if i % 2 != 0:
            L[i] = 0

    print(L)

    for i in range(len(L)):
        if i % 2 == 0:
            L.append(1)
            L.append(1)

    print(L)


# Zadanie 12
def task_12():
    L = eval(input("Enter a list of numbers: "))
    average = sum(L) / len(L)

    L.sort()

    print(f"average {average}")
    print(f"smallest 3 are {L[:3]}")
    print(f"Average without smallest: {(sum(L[1:]) / len(L[1:]))}")


# Zadanie 13
def task_13():
    L = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December"]
    index = eval(input("Enter the month number: "))

    print(L[index - 1])


# Zadanie 14
def task_14():
    L = []

    for i in range(1, 11):
        for j in range(i):
            L.append(i)

    print(L)


# Zadanie 15
def task_15():
    lista1 = eval(input("Enter a list of numbers: "))
    lista2 = eval(input("Enter a list of numbers (same length as previous): "))

    new_list = []

    for i in range(len(lista1)):
        if lista1[i] > lista2[i]:
            new_list.append(lista1[i])
        else:
            new_list.append(lista2[i])

    print(new_list)


# Zadanie 16
def task_16():
    lista = eval(input("Enter a list of numbers: "))
    L = []

    for i in range(len(lista)):
        L.append(sum(lista[:i + 1]))

    print(L)


# Zadanie 17
def task_17():
    n = eval(input("Enter a number: "))

    L = list(range(1, n + 1))
    lista = []
    for i in range(len(L)):
        lista.append(sum(L[:i + 1]))

    print(lista)


# Zadanie 18
def task_18():
    print("Enter 2 lists of numbers (both the same size): ")
    lista1 = eval(input("Enter a list of numbers: "))
    lista2 = eval(input("Enter a list of numbers: "))

    new_list = []

    for i in range(len(lista2)):
        new_list.append(lista1[i])
        new_list.append(lista2[i])

    print(new_list)


# Zadanie 19
def task_19():
    lista = eval(input("Enter a list of numbers: "))
    save = lista[0]

    for i in range(len(lista) - 1):
        lista[i] = lista[i + 1]

    lista[-1] = save
    print(lista)


# Zadanie 20
def task_20():
    import random as r
    repeats = []
    lista = []
    for i in range(20):
        number = r.randint(0, 2)
        lista.append(number)

    for i in range(1, len(lista) - 1):
        if lista[i] == lista[i - 1]:
            repeats.append(i)

    print(lista)
    print(f"repeats at indexes = {repeats}")


# Zadanie 21
def task_21():
    users_list = eval(input("Enter a list of numbers (at least 6 numbers): "))
    users_list.reverse()
    lista = users_list[:4]

    for i in range(len(users_list) - 1, 3, -1):
        lista.append(users_list[i])

    print(lista)

    users_list = eval(input("Enter a list of numbers (at least 6 numbers): "))

    L = users_list[:4][::-1] + users_list[4:]

    print(L)


# Zadanie 22
def task_22():
    string = input("Enter a word: ").lower()
    L = []
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        count = string.count(i)
        L.append(count)
    print(L)


# Zadanie 23
def task_23():
    import random

    lista = []
    index_50 = []
    for i in range(100):
        lista.append(random.randint(1, 50))

    for i in range(len(lista)):
        if lista[i] == 50:
            index_50.append(i)

    if len(index_50) >= 2:
        lista[index_50[0]] = -999
        lista[index_50[1]] = -999
    elif len(index_50) == 1:
        lista[index_50[0]] = -999
    else:
        print("no 50s")

    print(lista)


# Zadanie 24
def task_24():
    import random as r

    count = 0
    for i in range(10000):
        dice = []
        for j in range(5):
            number = r.randint(1, 6)
            dice.append(number)
        dice.sort()

        if dice == [1, 2, 3, 4, 5] or dice == [2, 3, 4, 5, 6]:
            count += 1

    print(f"the odds are {count / 10000}")


# Zadanie 26
def task_26():
    import random as r

    user_input = (input("Enter a list of numbers separated by spaces: "))
    lista = user_input.split()

    for i in range(len(lista)):
        random_index = r.randint(i, len(lista) - 1)
        lista[i], lista[random_index] = lista[random_index], lista[i]

    print(lista)


# Zadanie 27
def task_27():
    users_strings = input("Enter a list of strings separated by spaces: ")
    users_indices = input("Enter a list of indices that you would like to delete separated by spaces: ")

    list_of_strings = users_strings.split()
    list_of_indices = [int(x) for x in users_indices.split()]

    new_list = []

    for i in range(len(list_of_strings)):
        if not i in list_of_indices:
            new_list.append(list_of_strings[i])

    print(new_list)
