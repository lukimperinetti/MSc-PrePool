# ----- Variables ----- #

# TODO : Task 01
# Compute 1 + 11 + 111 + ... + 111111111.
# Also computes this number power 2, power 3, power 4, power 5, power 6 and power 7
print('TASk 01 :')


def calc(n):
    if n <= 0:
        return (0)
    else:
        return n + calc(n // 10)


number = int(input('entre le plus grand nombre a calculer : '))
res = calc(number)
print(res)
print('***********************************')
# TODO : Task 02
# Computes 17**1024 in less than 10 lines of code.
base = int(input('Entrez la base : '))
power = int(input('Entrez la puissance : '))
finaly = pow(base, power)
print(finaly)
