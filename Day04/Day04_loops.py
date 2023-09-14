# ----- Loops ----- #

def task00():
    int = 0
    while int <= 1000:
        print(int)
        int += 1

def task01():
    string = input('Entez une string >>> ')
    double_string = ''
    for letters in string:
        double_string += letters*2
    print(double_string)

def task02():
    start = 10000
    end = 1

    for cnt in range(start, end, -1):
        if( cnt%7==0 ):
            print(cnt)

def task03():
    minus = -30
    max = 30
    for cnt in range(minus, max):
        if (cnt%3)==0:
            print('Fizz')
        elif (cnt%5)==0:
            print('Buzz')
        elif (cnt%3)==0 and (cnt%5)==0:
            print('FizzBuzz')
        else :
            print(cnt)

def task04():
    lyrics = "99 bottles of age appropriate bottle on the wall"
    s = ''.join(x for x in lyrics if x.isdigit())
    converted = int(s)
    while converted >= 0:
        print(f'{converted} bottles of age appropriate bottle on the wall')
        converted -= 1
    

def task05():
    integer = int(input('Entrez un INT >>> '))
    end = integer//2
    start = 2
    multiple = []
    for cnt in range(start, end+1):
        multiple = []
        for num in range(start, integer):
            if (num%cnt)==0 :
                multiple.append(num)
        start += 1
        print(multiple[::-1])

def challenge():
    integer = int(input('entrez un int >>> '))
    string = input('Entrez une string')
    vowels = {"a", "e", "i", "o", "u", "A", "E", "I", "O", "U"}

    if integer == 0 : 
        return 0
    elif any(char in vowels for char in string):
        print(integer)
    elif integer >= 42:
        print(integer)
    else:
        print(string)


# task00()
# task01()
# task02()
# task03()
# task04()
task05() #TODO : a faire
# challenge()