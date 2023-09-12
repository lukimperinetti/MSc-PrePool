# ----- Modulo ----- #
import math

# TODO : Task 01
def task01():
    print('Task 01 :')
    dividende = int(input('entrez le dividende : '))
    diviseur = int(input('entrez le diviseur : '))

    print(f'résultat : {dividende/diviseur} \nquotient : {dividende//diviseur} \nreste : {dividende%diviseur}')

# TODO : Task 02
def task02():
    print('Tack 02 :')
    number_to_check = int(input('entrez un nombre : '))
    if number_to_check % 2 == 0:
        print('even')
    else:
        print('odd')

# TODO Task 3
def task03():
    number_to_calc = input('entrez un nombre : ')
    total = sum(int(d) for d in number_to_calc)
    print(total)

# TODO : Task 04
def task04():
    number_to_calc = float(input('entrez un nombre : '))
    rounded = number_to_calc - (number_to_calc % 1)
    print(rounded)

# TODO : Task 05
def task05():
    number_to_calc = float(input('entrez un nombre : '))
    rounded = number_to_calc % 1
    print(str(rounded).strip('0.'))

# task01()
# task02()
# task03()
# task04()
task05()