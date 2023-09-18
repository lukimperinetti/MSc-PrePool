# ----- Higher-order functions ----- #

def task00():
    
    def func1(string, number):
        print("Function 1")
        count=0
        for i in string:
            if(i.islower()):
                count=count+1
                if count >= number:
                    return True
                else:
                    return False
    is_lower = func1(string, number)
    print(is_lower)


    def func2(string, number):
        print("World")

    def func3(string, number):
        print("!")

    def func4(string, number):
        print("Bye")

    def func5(string, number):
        print("World")


string = input('entrez une chaine de caractères: ')
number = int(input('entrez un nombre: '))

task00()