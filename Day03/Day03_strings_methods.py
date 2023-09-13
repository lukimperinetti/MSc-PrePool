# ----- Methods ----- #

def task00():
    word = input('Task00 >>>').lower()
    print(word)

def task01():
    # TODO : replace TU by TA
    string = "tutu on the tuki-kata will output tata on the taki-kata"
    new_string = string.replace("tu", "ta")
    print(new_string)

def task02():
    string = "hello world"
    position = string.find("a")
    print(f'renvoi -1 si pas trouvé {position}')

def task03():
    p = "abcdefghij"
    print(p[:: -2][:5][:: -1][3:])
    # :: -2 = reviens a faire start:end:step. le -2 commence par la fin et escape 2 caractère a chaque fois
    # :5 c'est "jusqu'a 5"
    # 3: c'est "a partir du 3eme"

def task04():
    p = "abcdefghij"
    print(p[7::2])

def task05_06():
    print('this is a string\n'*10)

def task07():
    s1 = "Hello"
    s2 = 42
    concat = s1 + str(s2)
    print(concat)

def task08():
    string1 = "42"
    string2 = "is"
    string3 = "the answer"
    concat = '"' + string1 + " " + string2 + " " + string3+ '"' + ' contain 16 '

    print(f" The string {concat} characters ).")

def challenge():
    string = "thE Cat’s tactic wAS tO surpRISE thE mIce iN tHE gArdeN".lower()
    list=["cat", "garden", "mice"]
    count = 0
    for i in list:
        if string.find(i):
            count += 1
    rev = string[::-1]
    for i in list:
        if rev.find(i) and rev.find(i) != -1:
            count += 1
    print(count)


# task00()
# task01()
# task02()
# task03()
# task04()
# task05_06()
# task07()
# task08()
challenge()