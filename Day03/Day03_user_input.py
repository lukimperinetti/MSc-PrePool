# ----- User Input ----- #
import re
from string import punctuation

def task00():
    name = input('Votre nom >>>')
    print(f'Hello {name}')

def task01():
    name = input('Votre nom >>>').capitalize()
    print(f'Hello {name}')

def task02():
    # Prompt the user for two numbers and then print “The sum of the two provided numbers is sum”.
    numbers = input('entrez Deux nombres séparé d\'un espace >>>' )
    calc = int(numbers[0]) + int(numbers[2])
    print(f'La somme des deux nombres est : {calc}')

def task03():
    typed = int(input('Entrez un truc pour connaitre le type : '))
    print(f'le type est : {type(typed)}')

def task04():
    # premier mot de chaque phrase en string
    string = "This is a test. Is it possible to fly? Good things come to those who never give up."

    tab = re.findall(r"[\w']+|[.,!?;]", string)
    print(tab)

    sentence = tab[0]  # Premier mot
    punctuations = re.findall("[.,!?;]+", string)

    for item in punctuations:
        index = string.find(item) + len(item)  # Obtenir la position de la ponctuation et avancer de sa longueur
        next_word = re.search(r"[\w']+", string[index:])

        if next_word:
            sentence += ' ' + next_word.group()  # Obtenir le premier mot après la ponctuation
            string = string[index + next_word.start():]  # Mettre à jour la chaîne pour continuer la recherche

    print(sentence)
    
# task00()
# task01()
# task02()
# task03()
task04()