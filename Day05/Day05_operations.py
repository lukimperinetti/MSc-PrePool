# ----- Operations on lists ----- #

import random


def task01():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    result = 1
    for elements in numbers:
        result=result*elements
    print(result)

def task02():
    print([x + 10 for x in [3, 2, 6, 7, 1, 4]])
    #Liste en compréhension
    # revient a faire : 
    # list = []
    # for x in [3, 2, 6, 7, 1, 4]:
    #     x += 10
    #     list.append(x)
    # print(list)
    

def task03():
    print(list(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))
    #list() = return une liste
    # map() = c'est un iterateur comme une boucle
    # lambda = prend un nombre en arg et ne peut avoir qu'un expression
    # ici x = x*x
    # Ici j'ai une boucle qui multiplie chaque eleme par lui meme

def task04():
    x = list(sorted(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))
    print(x[0], x[-1])

def task05():
    x = list(sorted(map(lambda x: x * x, [3, 2, 6, 7, 1, 4])))
    print([all for all in x if all < 7])

def task06():
    x = list(sorted(map(lambda x: x * x, [3, 2, 6, 7, 1, 4]), reverse=True))
    print(x)

def task07():
    print([x // 2 if x % 2 == 0 else x * 2 for x in [42, 3, 4, 18, 3, 10]])

    # on affiche X sans décimales a condition qu'il soit un multiple de 2
    # sinon on le multiplie par 2 
    # et ca pour chaques X de la liste
    # list = []
    # for x in [42, 3, 4, 18, 3, 10]:
    #     if x % 2 == 0:
    #         list.append(x//2)
    #     else:
    #         list.append(x*2)
    # print(list)

def task08():
    print(list(filter(lambda x: x > 10, [42, 3, 4, 18, 3, 10])))
    
    #Je choisis d'apliquer un filtre sur ma liste.
    # Ici je ne veux rien afficher en dessous de 10

def task09():
    print([*enumerate([42, 3, 4, 18, 3, 10])])
    # enumerate perment de renvoyer l'index de chaque elem de la list

def task10():
    first_name = ["Jackie", "Bruce", "Arnold", "Sylvester"]
    last_name = ["Stallone", "Schwarzenegger", "Willis", "Chan"]
    magic = [*zip(first_name, last_name [:: -1])]
    print(magic [0])
    print(magic [3])
    print(magic [1][0])
    print(magic [0][1])
    print(magic [2])
    # zip permet de lier des listes et de ne chercher que via 1 seul appel


def challenge():
    randomlist = []
    for i in range(0,1000000):
        n = random.randint(1,1000000)
        randomlist.append(n)
    print(randomlist)


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
challenge()