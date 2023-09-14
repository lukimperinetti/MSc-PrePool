# ----- Conditionals ----- #

# def task00():
# Evaluate and explain the following lines:
#   (42 > 12) --> True
#   (12 = 12) --> err ?
#   (12 == 12) --> true
#   (“hello” == “world”) --> false
#   (218 >= 118) --> true
#   (“a”.upper() == “A”) --> true 
#   (1 ∗ 2 ∗ 3 ∗ 4 <= 9) --> false 
#   (“z” in “azerty”) --> true

def task01():
    integer = int(input('Entrez un int >>> '))
    if integer == 42:
        print('Correct answer')
    else:
        print('Error, expected : 42')

def task02():
    integer = int(input('Entrez un int >>> '))
    if (integer % 2) == 0:
        print('This integer is odd')
    else:
        print('This integer is even')

def task03():
    string = input('Entrez une phrase >>> ').lower()

    if string == "open sesame":
        print('access granted')
    elif string == "will you open, you goddamn !¤*@¡":
        print("access fucking granted")
    else:
        print('permission denied')


# TODO : a optimiser quand je m'ennuis évidemment
def task04():
    integer = int(input('Entrez un int >>> '))

    if integer == 42:
        print('OK')
    elif integer <= 21:
        print('OK')
    elif (integer%2) == 0:
        print('OK')
    elif (integer/2) < 20:
        print('OK')
        # finally, if it’s is odd and greater or equal than 45, display “OK” ;
    elif (integer%2) == 0 or integer == 45:
        print('OK')
    else:
        print('You got wrong my poor friend!')

def task05():
    a = 42
    b = 41
    if a == b:
        print ("A and B are the sames ")
    if b <= a:
        print ("B is equal or lower than A")
    if b != a:
        print ("B is different from A")



# task01()
# task02()
# task03()
# task04()
# task05()
