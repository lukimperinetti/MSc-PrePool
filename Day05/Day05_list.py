# ----- Lists creation and browsing ----- #

def task01():
    numbers = [1, 2, 3, 4, 5]
    print(numbers[0])


def task02():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(numbers[-1])

def task03():
    numbers = [1, 2, 3, 4, 5, 6]
    numbers.append(7)
    print(numbers)

def task04():
    numbers = [1, 2, 3, 4, 5, 6, 7]
    print(numbers)

def task05():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers.pop(-1)
    print(numbers)

def task06():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers.insert(0, 'premier')
    print(numbers)

def task07():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers[1:5])

def task08():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    numbers.reverse()
    print(numbers)

def task09():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(numbers[0::2])

def task10():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    i = numbers[-1]
    count = 0
    while count < 17:
        numbers.append(i+1)
        i += 1
        count += 1
    print(numbers)

def task11():
    # my_first_list = [4, 5, 6]
    # my_second_list = [1, 2, 3]
    # my_first_list.extend(my_second_list)
    # print(my_first_list) # ajoute les elem de la seconde liste a la premiere

    my_first_list = [7, 8, 9]
    my_second_list = [4, 5, 6]
    my_first_list = [*my_first_list, *my_second_list]
    print(my_first_list) # pareil sans l'utilisation d'une methode



# task01()
# task02()
# task03()
# task04()
# task05()
# task06()
# task07()
# task08()
# task09()
# task10()
task11()