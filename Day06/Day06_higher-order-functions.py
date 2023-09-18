# ----- Higher-order functions ----- #

import re


def task00():

    def func1(string, number):
        print("Function 1")
        count=0
        for i in string:
            if i.islower():
                count += 1
                if count >= number:
                    return True
        return False

    is_lower = func1(string, number)
    print(is_lower)


    def func2(string, number):
        print("Function 2")
        count=0
        for i in string:
            if i.isupper():
                count += 1
                if count >= number:
                    return True
        return False
    is_upper = func2(string, number)
    print(is_upper)

    def func3(string, number):
        print("Function 3")
        count=1
        for i in string:
            if count >= number:
                return True
            count += 1
        return False
    counted = func3(string, number)
    print(counted)

    def func4(string, number):
        print("Function 4")
        count=1
        regex = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
        for i in string:    
            if count >= number and regex.search(string) == None:
                return True
            count += 1
        return False
    special_char = func4(string, number)
    print(special_char)

    def func5(string, number):
        print("Function 5")
        count=1
        for i in string:
            if i.isdigit() and count >= number  :
                return True
            count += 1
        return False
    digit = func5(string, number)
    print(digit)


string = input('entrez une chaine de caractères: ')
number = int(input('entrez un nombre: '))

task00()