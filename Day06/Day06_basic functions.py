# ----- Basic Function ------ #

def task00():
    # explain this function : 
    # une fonction prend un paramètre X a sa création et 
    # retourne une valeur Y à la fin de son exécution
    # a son appel, on l'initialise avec un paramètre X
    def f(x):
        return 2 * x + 1
    def g():
        return 7
    y = f(2)
    print(y)
    y = f(5) + g()
    print(y)

def task01():
    def  bread ():
        print("<//////////>")
    def  lettuce ():
        print("~~~~~~~~~~~~")
    def  tomato ():
        print("O O O O O O")
    def  ham():
        print("============")

    bread()
    lettuce()
    tomato()
    ham()
    ham()
    bread()

def task02():
    def  bread ():
        print("<//////////>")
    def  lettuce ():
        print("~~~~~~~~~~~~")
    def  tomato ():
        print("O O O O O O")
    def  ham():
        print("============")

    i=0
    while i<42:
        bread()
        lettuce()
        tomato()
        ham()
        ham()
        bread()
        print("\n")
        i+=1



def task03(x):
    def  bread ():
        print("<//////////>")
    def  lettuce ():
        print("~~~~~~~~~~~~")
    def  tomato ():
        print("O O O O O O")
    def  ham():
        print("============")

    if int(x) <= 0:
        print('I can\'t do this')
        return 0
    else :
        i=0
        while i<int(x):
            bread()
            lettuce()
            tomato()
            ham()
            ham()
            bread()
            print("\n")
            i+=1
   
def task04(x):
    def  bread ():
        print("<//////////>")
    def  lettuce ():
        print("~~~~~~~~~~~~")
    def  tomato ():
        print("O O O O O O")
    def  ham():
        print("============")

    if int(x) <= 0:
        print('I can\'t do this')
        return 0
    else :
        choice = input("Do you want vegan sandwich ? (y/n) >>> ")
        if choice == 'n':
            i=0
            while i<int(x):
                bread()
                lettuce()
                tomato()
                ham()
                ham()
                bread()
                print("\n")
                i+=1
        elif choice == 'y':
            i=0
            while i<int(x):
                bread()
                lettuce()
                tomato()
                bread()
                print("\n")
                i+=1
        else :
            print('I don\'t understand')
            return 0
        

def challenge():
    def power():
        return 42**84
    power()


# If you want to know precisely how long the execution of 
# your program lasted, you can put the 
# codestartingTime = time.time()at the beginning and
# duration = time.time()- startingTime at the end.6



# task01()
# task02()
# task03(input("How many sandwiches do you want ? >>> "))
# task04(input("How many sandwiches do you want ? >>> "))
challenge()