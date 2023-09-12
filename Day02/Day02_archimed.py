# ----- Archimed ----- #

def task01():
    # π = (4/1) - (4/3) + (4/5) - (4/7) + (4/9) - (4/11) + (4/13) etc etc ...

    print('Entrez un nombre. Plus il est élevé, plus le calcul sera précis')
    precis = int(input('>>> '))

    resultat = 0
    denominateur = 1
    signe = 1

    while precis > 0:
        terme = signe * (4 / denominateur)
        resultat += terme
        denominateur += 2
        signe *= -1
        precis -= 1

    print('Le résultat de la somme est :', round(resultat, 6))


def calc_pi(i):
    pi = 3.141592

    res = round(i**2 / 6, 6)

    if res == pi:
        print(f'{res} success')  # Utilisez f-string pour inclure des variables dans la chaîne
        return 1
    elif res > pi:
        print('error')
        return 0
    else:
        res = round(res + calc_pi(i + 2), 6)
        print(f'coucou {res}')
        print('je calcule')  # Correction de la faute de frappe
        return 1
        # compare + résultat de i**2 / 6
        # i + 2 (1 3 5 7)

result = calc_pi(1)
print(f"Resultat final : {result}")




# i = 1
# res = i ** 2 / 6, 6
# pi = 3.141592
# while float(res) < pi:
#     res = res + (i + 2)**2 + 6, 6
#     print(res)


# task01()
# calc_pi(1)
